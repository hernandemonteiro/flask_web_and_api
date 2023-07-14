from flask import Flask, jsonify, render_template
from utils.markdown import render_markdown
from models.DocPage import DocPage


app = Flask(__name__)

links = [
    DocPage("/pt-br/techs", "Dev Techs", "docs/pt-BR/technologies.md"),
    DocPage("/pt-br/nextjs", "NextJS", "docs/pt-BR/nextjs.md"),
    DocPage("/pt-br/o_codificador", "O Codificador",
            "docs/pt-BR/o_codificador.md")
]


@app.route("/")
def hello():
    return render_template("hello.html", name="Hernande Monteiro",
                           pages=links)


@app.route("/project_infos")
def getProjectInfos():
    return jsonify([{
        "Author": "Hernande Monteiro",
        "Framework": "Flask",
        "repository_name": "solutions",
        "github:repo": "https://github.com/hernandemonteiro/solutions",
        "server": "vercel/@python"
    }])


@app.route(links[0].link)
def techs():
    return render_markdown(links[0].file,
                           links[0].title)


@app.route(links[1].link)
def nextjs():
    return render_markdown(links[1].file,
                           links[1].title)


@app.route(links[2].link)
def o_codificador():
    return render_markdown(links[2].file,
                           links[2].title)


if (__name__ == "__main__"):
    app.run(host="0.0.0.0")
