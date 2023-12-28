#!/usr/bin/python3
""" script that starts flask wep app """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ main page - displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ display HBNB """
    return "HBNB"


@app.route("/c/<text>")
def text(text):
    """ display variable route """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def pyt(text):
    """ display variable route """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:text>")
def number(text):
    """ display variable is a number """
    return "{} is a number".format(text)


@app.route("/number_template/<int:n>")
def number_template(n):
    """ display html page if n is int """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
