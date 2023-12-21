import os
import gzip
import shutil

def unzip_gz_file(gz_file_path, output_file_path):
    with gzip.open(gz_file_path, 'rb') as gz_file:
        with open(output_file_path, 'wb') as output_file:
            shutil.copyfileobj(gz_file, output_file)

# Example usage:
gz_file_path = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/consolidated_destination/42/consolidated/transaction/1-478-W-2023-42-volume-per-transaction.csv.gz'
output_folder = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/consolidated_destination/42/consolidated/transaction/unzipped/'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Build the output file path
output_file_path = os.path.join(output_folder, os.path.basename(gz_file_path.replace('.gz', '')))

# Unzip the file
unzip_gz_file(gz_file_path, output_file_path)
