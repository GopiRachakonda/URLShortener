# URL Shortener

This is a simple URL shortener service built with Flask and Redis. It allows users to shorten URLs, retrieve the original URL using the shortened URL, and track the number of clicks.

## Features
- Shorten any URL.
- Redirect to the original URL via a shortened URL.
- Track URL analytics (click counts).

## Requirements
- Python 3.x
- Redis (locally or through a cloud provider)

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd url_shortener
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start Redis locally (or configure a remote Redis instance):
    ```bash
    redis-server
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://localhost:5000/` to use the URL shortener.

## Usage
1. Enter a URL in the input field on the homepage.
2. You will get a shortened URL (e.g., `http://localhost:5000/abcd12`).
3. Access the shortened URL to be redirected to the original URL.
4. Check the analytics by visiting `http://localhost:5000/analytics/<shortened-url>`.
