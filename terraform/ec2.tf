resource "aws_instance" "fastapi_server" {
  ami             = "ami-1234567890abcdef0"  # Ubuntu AMI example
  instance_type   = var.instance_type
  key_name        = "my-key-pair"  # Ensure you have a valid key pair
  security_groups = [aws_security_group.web_sg.name]

  tags = {
    Name = "FastAPI-Server"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install python3-pip -y",
      "pip3 install fastapi uvicorn",
      "git clone <YOUR_REPO_URL>",
      "cd YOUR_REPO_NAME",
      "uvicorn main:app --host 0.0.0.0 --port 8000"
    ]
  }
}

resource "aws_instance" "react_frontend" {
  ami             = "ami-1234567890abcdef0" 
  instance_type   = var.instance_type
  key_name        = "my-key-pair"  
  security_groups = [aws_security_group.web_sg.name]

  tags = {
    Name = "React-Frontend"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install nodejs npm -y",
      "git clone <YOUR_REPO_URL>",
      "cd YOUR_REPO_NAME/frontend",
      "npm install",
      "npm start"
    ]
  }
}
