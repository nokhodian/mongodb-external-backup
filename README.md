```markdown
# MongoDB Backup to AWS S3 with Terraform 🌍💾

Automate the backup of MongoDB databases and store them securely in AWS S3 using Python and Terraform. This guide includes setting up an AWS S3 bucket using Terraform and a Python script to backup MongoDB instances and upload the backups to S3.

## Prerequisites 📋

- Python 3.8+ 🐍
- Terraform 1.0+ 🛠️
- AWS CLI configured with user credentials 🔑
- pip for Python package management 📦

## Installation 🚀

### Clone the Repository 📂

```shell
git clone https://github.com/nokhodian/mongodb-external-backup.git
cd mongodb-external-backup
```

### Install Python Dependencies 🐍

```shell
pip install boto3 pymongo python-dotenv
```

### Configure Environment Variables 🔧

Create a `.env` file in the project root with your MongoDB and AWS settings:

```env
MONGO_INSTANCES=[{"name": "instance1", "connection_string": "mongodb+srv://user1:password1@host1/database1", "wait_seconds": 10}, {"name": "instance2", "connection_string": "mongodb+srv://user2:password2@host2/database2", "wait_seconds": 20}]
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_BUCKET_NAME=your_bucket_name
AWS_REGION=your_aws_region
TOTAL_WAIT=wait_time_betweenbackups_in_seconds
```

### Terraform S3 Bucket Setup 🪣 (you can create your s3 bucket on your side or use this script)

Navigate to the Terraform configuration directory:

```shell
cd terraform
```

Initialize Terraform:

```shell
terraform init
```

Apply the Terraform configuration to create the S3 bucket:

```shell
terraform apply
```

Confirm the creation when prompted.

## Usage 🔄

### Running the Backup Script 📜

Execute the Python script to start the backup process:

```shell
python main.py
```

The script reads MongoDB instance details from the `.env` file, creates backups, uploads them to the specified S3 bucket, and deletes the local backup files.

## Notes 📝

- Ensure your AWS IAM user has permissions for S3 bucket creation and object management.
- Adjust MongoDB and AWS settings in the `.env` and Terraform files as needed.
- The `wait_seconds` parameter in `MONGO_INSTANCES` controls the delay between consecutive backups.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```
