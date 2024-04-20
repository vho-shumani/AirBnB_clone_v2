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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
