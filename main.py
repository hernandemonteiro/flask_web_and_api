from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html", name="Hernande Monteiro")


@app.get("/project_infos")
def getFunction():
    # body of request
    req = request.form
    # to return a json list you need call the jsonify function
    return jsonify([{
        "author": "Hernande Monteiro",
        "Framework": "Flask",
        "name": "flask_web_and_api",
        "request": req
    },
        {
        "developer": "Hernande Monteiro",
        "Framework-Version": "2.0.2",
    }])


if (__name__ == "__main__"):
    app.run(debug=True)
