# Este Projeto (Notas e Docs)

Projeto desenvolvido em flask que documenta ferramentas e anotações obtidas no decorrer de meus desenvolvimentos.

A ideia é capturar conhecimento com as práticas utilizadas em projetos e estudos para desenvolver boas práticas de código e segurança em aplicações e serviços.

Todas as rotas são escritas em markdown, facilitando reuso caso necessário e em breve sumario no github.

# Infra as Code

Uso de terraform para provisionar instância de EC2 na aws e
Ansible para trabalhar com versionamento de código.
# Project Structure

`main.py`: define as rotas e funções/metodos a serem chamados.
`/templates`: todos os templates em html utilizados no projeto.
`/static`: arquivos staticos como images.
`terraform_flask_run`: todos arquivos do Terraform e Ansible
`/venv`: virtual environment do projeto.
`.vscode`: configurações de estilo do editor.
