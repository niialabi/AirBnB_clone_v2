#!/usr/bin/python3
""" script that starts flask wep app """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route("/", strict_slashes=False)
def hello():
    """ main page - displays Hello HBNB! """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display HBNB """
    return "HBNB"

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5000")
