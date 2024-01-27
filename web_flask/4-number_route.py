#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route:
    '/' displayes "Hello HBNB!"
    /hbnb - dislays "HBNB"
    /c/<text> - displays "C <text>
    /python/<text> - displays "Python is cool"
    /number/<n> - display n if integer
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_text(text):
    """Displays C"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Prints python is cool"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """Displays n if integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
