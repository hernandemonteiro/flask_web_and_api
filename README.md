#### `Projeto em desenvolvimento!`

# Este Projeto (Notas e Docs)

Projeto desenvolvido em flask para documentar ferramentas e anotações obtidas no decorrer de meus desenvolvimentos.

A ideia é capturar conhecimento com as práticas utilizadas em projetos e estudos para desenvolver boas práticas de código e segurança em aplicações e serviços.

Todas as rotas são escritas em markdown, facilitando reuso caso necessário e em breve sumario no github.

# Adicionar Página

basta criar o arquivo ".md" em `/docs/` e após adicionar uma nova instancia da classe `DocPage` a lista `links` no arquivo `/main.py`.

# Infra as Code

Uso de terraform para provisionar instância de EC2 na aws e
Ansible para trabalhar com versionamento de código.

# Project Structure

`main.py`: define as rotas e funções/metodos a serem chamados.
<br/>

`/docs`: todos os docs, divididos por idioma(pt-br, ...).

`/templates`: todos os templates em html utilizados no projeto.
<br/>

`/static`: arquivos staticos como images.
<br/>

`/models`: Camada de modelos "MVC".
<br/>

`/utils`: código reutilizavel ou helpers.
<br/>

`terraform_flask_run`: todos arquivos do Terraform e Ansible.
<br/>

`/venv`: virtual environment do projeto.
<br/>

`/notes.md`: notas referente a configurações deste projeto.
<br/>

`/package.json`: scripts in node to automate deploy;
<br/>

`/requirements.txt`: dependências do projeto.
