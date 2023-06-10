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
  tags = {
    Name = "flask_runner"
  }
}
