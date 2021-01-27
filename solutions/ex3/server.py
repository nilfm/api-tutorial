from flask import Flask, abort
import json

app = Flask(__name__)

data = {
    "Nil": {
        "age": 21,
        "subject": "topology",
    },
    "Anna": {
        "age": 18,
        "subject": "programming",
    },
    "Mar": {
        "age": 18,
        "subject": "calculus",
    },
    "Joel": {
        "age": 18,
        "subject": "algebra",
    },
    "Kamil": {
        "age": 18,
        "subject": "hardware",
    },
    "Joan": {
        "age": 19,
        "subject": "physics",
    },
}

@app.route("/users", methods=["GET"])
def users():
    names = list(data.keys())
    return json.dumps(names)

@app.route("/user/<string:name>", methods=["GET"])
def user(name):
    try:
        info = data[name]
        info["name"] = name
        return json.dumps(info)
    except:
        abort(404)

if __name__ == "__main__":
    app.run()