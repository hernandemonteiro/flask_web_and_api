terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "hm_solution_server" {
  ami           = "ami-03f65b8614a860c29"
  instance_type = "t2.micro"
  key_name      = "flask-terraform"
  user_data     = <<-EOF
                      #!/bin/bash
                      cd /home/ubuntu
                      echo “<h1>Mensagem a ser mostrada</h1>” > index.html
                      nohup busybox httpd -f -p 8080 &
                      mkdir hellodir
                      sudo git clone https://github.com/hernandemonteiro/flask_web_and_api
                      EOF
  tags = {
    Name = "flask_runner"
  }
}
