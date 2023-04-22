#!/usr/bin/python3
"""flask app that runs when called"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_lang(text="is cool"):
    new_word = text.replace('_', ' ')
    return "Python {}".format(new_word)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/c/<text>', strict_slashes=False)
def prog(text):
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
