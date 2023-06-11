from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html", name="Hernande Monteiro")


@app.get("/project_infos")
def getFunction():
    return jsonify([{
        "Author": "Hernande Monteiro",
        "Framework": "Flask",
        "repository_name": "flask_web_and_api",
    }])


if (__name__ == "__main__"):
    app.run(host="0.0.0.0")
