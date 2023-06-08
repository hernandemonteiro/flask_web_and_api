from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html")


@app.get("/get")
def getFunction():
    return {
        "name": "Hernande Monteiro",
        "method": "GET",
        "Framework": "Flask",
        "Response": "Json - Dict"
    }


app.run(port=3000, debug=True)
