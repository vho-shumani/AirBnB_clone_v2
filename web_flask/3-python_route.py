#!/usr/bin/python3
"""Start a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Defines a view function for root url.
    Returns: (str) text message
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Defines a view function for /hbnb url.
    Returns: (str) text message
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    Defines a view function for /c/<text> url.
    Returns: (str) text message
    """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """
    Defines a view function for /python/<text> url.
    Returns: (str) text message
    """
    text = text.replace("_", " ")
    return f"python {text}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
