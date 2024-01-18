import os
import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_path, bucket_name, s3_path):
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        if os.path.isfile(local_path):
            # Upload a file, skip .DS_Store
            if not local_path.endswith('.DS_Store'):
                filename = os.path.basename(local_path)
                s3.upload_file(local_path, bucket_name, os.path.join(s3_path, filename))
                print(f"Uploaded {local_path} to {s3_path}.")
            else:
                print(f"Skipped {local_path}.")
        elif os.path.isdir(local_path):
            # Upload a directory (recursively), skip .DS_Store
            for root, dirs, files in os.walk(local_path):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    if not local_file_path.endswith('.DS_Store'):
                        s3_file_path = os.path.join(s3_path, os.path.relpath(local_file_path, local_path))
                        s3.upload_file(local_file_path, bucket_name, s3_file_path)
                        print(f"Uploaded {local_file_path} to {s3_file_path}.")
                    else:
                        print(f"Skipped {local_file_path}.")
        else:
            print(f"{local_path} is neither a file nor a directory.")

        print("Upload successful.")
    except NoCredentialsError:
        print("Credentials not available.")

if __name__ == "__main__":
    # Replace with your S3 bucket details
    bucket_name = 'payout-recon'

    # Replace with your local file or folder path
    local_path = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/txn/2024/fundsRxd/'

    # Replace with the desired S3 path
    s3_path = 'ppro/txn/funds-received/raw/past-data/2024/'

    # Upload to S3
    upload_to_s3(local_path, bucket_name, s3_path)
