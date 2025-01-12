resource "mongodbatlas_project" "my_project" {
  name   = var.mongo_project_name
  org_id = "<Your MongoDB Atlas Org ID>"
}

resource "mongodbatlas_cluster" "my_cluster" {
  project_id   = mongodbatlas_project.my_project.id
  name         = var.mongo_cluster_name
  cloud_backup = true

  provider_name = "AWS"
  provider_region_name = "US_EAST_1"
  provider_instance_size_name = "M0"
  
  mongo_db_user {
    username = var.mongo_user
    password = var.mongo_password
    roles {
      role_name = "readWrite"
      database_name = "student_universe_db"
    }
  }
}
