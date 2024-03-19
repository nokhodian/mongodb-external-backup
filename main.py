import os
import json
import subprocess
from datetime import datetime
from time import sleep
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def backup_mongodb(connection_string, backup_name):
    backup_cmd = f"mongodump --uri=\"{connection_string}\" --archive={backup_name} --gzip"
    subprocess.run(backup_cmd, shell=True)

def upload_to_s3(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client = boto3.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'), region_name=os.getenv('AWS_REGION'))
    response = s3_client.upload_file(file_name, bucket_name, object_name)
    return response

def main():
    instances = json.loads(os.getenv('MONGO_INSTANCES'))
    bucket_name = os.getenv('AWS_BUCKET_NAME')
    total_wait = os.getenv('TOTAL_WAIT')
    while True:
        for instance in instances:
            backup_name = f"{instance['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.gz"
            print(f"Backing up {instance['name']} to {backup_name}")
            backup_mongodb(instance['connection_string'], backup_name)
            print(f"Uploading {backup_name} to S3")
            upload_to_s3(backup_name, bucket_name)
            os.remove(backup_name)
            print(f"Backup and upload for {instance['name']} completed.")
            sleep(instance[50])
        sleep(total_wait)

if __name__ == "__main__":
    main()
