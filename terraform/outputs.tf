output "fastapi_public_ip" {
  value = aws_instance.fastapi_server.public_ip
}

output "frontend_public_ip" {
  value = aws_instance.react_frontend.public_ip
}

output "mongo_cluster_url" {
  value = mongodbatlas_cluster.my_cluster.connection_strings[0]
}
