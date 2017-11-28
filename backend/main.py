# -*- coding: utf-8 -*-

try:
    from os import getuid

except ImportError:
    def getuid():
        return 4000

from flask import Flask, render_template, json, Response, Request


app = Flask(__name__)


@app.route("/")
@app.route("/hello/<text>")

def hello(text="Bonjour"):
    return render_template("index.html", text=text)

@app.route("/data")
def index():
    return json.jsonify(
    {"a": request.args.get("a")}
)


if __name__ == "__main__":
    app.run(port=getuid() + 1000, debug=True)
