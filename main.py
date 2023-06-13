from flask import Flask, render_template, jsonify
from utils.markdown import render_markdown
from models.DocPage import DocPage


app = Flask(__name__)

links = [
    DocPage("/pt-br/techs", "Dev Techs", "docs/pt-BR/technologies.md"),
    DocPage("/pt-br/nextjs", "NextJS", "docs/pt-BR/nextjs.md"),
]


@app.route("/")
def hello():
    return render_template("hello.html", name="Hernande Monteiro", pages=links)


@app.get("/project_infos")
def getFunction():
    return jsonify([{
        "Author": "Hernande Monteiro",
        "Framework": "Flask",
        "repository_name": "solutions",
        "github:repo": "https://github.com/hernandemonteiro/solutions",
        "server": "AWS EC2"
    }])


for route in links:
    @app.route(route.link)
    def techs():
        return render_markdown(route.file,
                               route.title)


if (__name__ == "__main__"):
    app.run(host="0.0.0.0")
