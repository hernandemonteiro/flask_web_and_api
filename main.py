from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html")


@app.get("/project_infos")
def getFunction():
    return {
        "author": "Hernande Monteiro",
        "Framework": "Flask",
        "name": "flask_web_and_api"
    }


if (__name__ == "__main__"):
    app.run()
