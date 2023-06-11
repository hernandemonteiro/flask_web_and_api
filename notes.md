# Pre-Configs EC2

para que a aplicação funcione bem precisamos criar um arquivo do tipo `service` na maquina provisionada,
este arquivo vai ser reiniciado a cada
iteração do ansible.

host and port:
`0.0.0.0:5000`

caminho do arquivo:
`/etc/systemd/system`

nome do arquivo:
`flask_runner.service`

conteudo:

```
[Unit]
Description=Gunicorn instance for a simple hello world app
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/flask_web_and_api
ExecStart=/home/ubuntu/flask_web_and_api/venv/bin/gunicorn -b 0.0.0.0:5000 main:app
Restart=always
[Install]
WantedBy=multi-user.target

```

comando para criação:
`sudo nano /etc/systemd/system/flask_runner.service`

após configurado rodar os seguintes comandos:

```

sudo systemctl daemon-reload
sudo systemctl start flask_runner
sudo systemctl enable flask_runner

```

\* para reiniciar o serviço com novos arquivos usar o método restart do systemctl
