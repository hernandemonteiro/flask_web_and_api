from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    # and to acess in the html the variable we need {{...}}, but
    # in case of iteration
    # likes for we needs {%...%}
    return render_template("hello.html", name="Hernande Monteiro")


@app.get("/project_infos")
def getFunction():
    req_body = request.form

    # to return a json list you need call the jsonify function
    return jsonify([{
        "author": "Hernande Monteiro",
        "Framework": "Flask",
        "name": "flask_web_and_api",
        "request": req_body
    },
        {
        "developer": "Hernande Monteiro",
        "Framework-Version": "2.0.2",
    }])


if (__name__ == "__main__"):
    app.run(debug=True)
