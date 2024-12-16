from flask import Flask, render_template, request, redirect
import redis
import hashlib

app = Flask(__name__)

# Connect to Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    if not url:
        return "URL is required", 400

    # Generate a short URL, e.g., 'abcd12'
    short_url = shorten_url(url)

    # Store the original URL in Redis using the short URL as the key
    r.set(short_url, url)
    print(f"Stored shortened URL {short_url} in Redis")

    # Initialize click count for analytics
    r.hset("analytics", short_url, 0)

    return f"Shortened URL: <a href='/{short_url}'>/{short_url}</a>"

@app.route('/<short_url>')
def redirect_to_url(short_url):
    # Retrieve the original URL from Redis
    original_url = r.get(short_url)

    if original_url:
        # Increment the click count for analytics
        r.hincrby("analytics", short_url, 1)
        return redirect(original_url)
    else:
        return "URL not found", 404

@app.route('/analytics/<short_url>')
def analytics(short_url):
    # Get click count from Redis analytics hash
    click_count = r.hget("analytics", short_url)

    if click_count:
        return jsonify({"short_url": short_url, "click_count": int(click_count)})
    else:
        return "Analytics data not found", 404

def shorten_url(url):
    # Use a hash function (e.g., MD5 or SHA256) to generate a shortened URL
    short_hash = hashlib.md5(url.encode()).hexdigest()[:6]
    return short_hash

if __name__ == '__main__':
    app.run(debug=True)
