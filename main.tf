provider "aws" {
  region = "us-east-1" # Replace with your desired AWS region
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "mongodb-backup-bucket" # Replace with your desired bucket name
  acl    = "private"

  versioning {
    enabled = true
  }

  lifecycle_rule {
    enabled = true

    noncurrent_version_expiration {
      days = 30
    }
  }

  tags = {
    Name        = "MongoDB Backups"
    Environment = "Production"
  }
}
