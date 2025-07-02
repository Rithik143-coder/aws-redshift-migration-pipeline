resource "aws_redshift_cluster" "default" {
  cluster_identifier = "redshift-cluster-1"
  database_name      = "target_dw"
  master_username    = "admin"
  master_password    = "YourPassword123"
  node_type          = "dc2.large"
  cluster_type       = "single-node"
}
