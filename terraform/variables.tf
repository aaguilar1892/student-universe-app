variable "aws_region" {
  default = "us-east-1"
}

variable "aws_access_key" {}
variable "aws_secret_key" {}

variable "instance_type" {
  default = "t2.micro"
}

variable "mongo_cluster_name" {
  default = "student_universe_cluster"
}

variable "mongo_project_name" {
  default = "student_universe_project"
}

variable "mongo_user" {}
variable "mongo_password" {}
