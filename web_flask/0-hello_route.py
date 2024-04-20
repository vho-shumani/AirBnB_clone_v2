#!/usr/bin/python3
"""Module starts flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Define a view function for the root url
    Returns: (str) a greeting message.
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
