from flask import Flask, render_template, jsonify
import markdown.extensions.fenced_code
from utils.markdown import template


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html", name="Hernande Monteiro")


@app.route("/pt-br/techs")
def technologies():
    readme_file = open("docs/pt-BR/technologies.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return template(md_template_string, "Tecnologias")


@app.get("/project_infos")
def getFunction():
    return jsonify([{
        "Author": "Hernande Monteiro",
        "Framework": "Flask",
        "repository_name": "flask_web_and_api",
        "github:repo": "https://github.com/hernandemonteiro/flask_web_and_api",
        "server": "AWS EC2"
    }])


if (__name__ == "__main__"):
    app.run(host="0.0.0.0")
