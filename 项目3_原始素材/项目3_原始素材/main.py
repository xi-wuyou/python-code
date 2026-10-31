from flask import Flask, render_template, jsonify, request
from unit3 import *
import os

file_path = os.path.abspath(__file__)
file_dir = os.path.dirname(file_path)

template_path = os.path.join(file_dir, 'templates')
static_path = os.path.join(file_dir, 'static')

app = Flask(__file__, template_folder=template_path, static_folder=static_path)


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/data")
def data():
    json = request.json
    return jsonify(
        {
            'result': main(json['nums'], json['type'])
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
