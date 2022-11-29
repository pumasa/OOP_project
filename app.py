from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    with open("scores.json") as json_data:
        data = json.load(json_data)

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
