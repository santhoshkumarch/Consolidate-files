import os
import gzip
import shutil
import pandas as pd
import glob

def unzip_gz_file(gz_file_path, output_file_path):
    with gzip.open(gz_file_path, 'rb') as gz_file:
        with open(output_file_path, 'wb') as output_file:
            shutil.copyfileobj(gz_file, output_file)

def process_csv_files(folder_path):
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

    for csv_file_path in csv_files:
        # Unzip the CSV file
        unzipped_file_path = os.path.join(folder_path, os.path.basename(csv_file_path.replace('.gz', '')))
        unzip_gz_file(csv_file_path, unzipped_file_path)

        # Read the unzipped CSV file into a DataFrame
        df = pd.read_csv(unzipped_file_path)

        # Perform modifications on the DataFrame
        # Example modification: Add a new column
        df['New_Column'] = 'Modified Value'

        # Save the modified DataFrame back to the unzipped CSV file
        df.to_csv(unzipped_file_path, index=False)

        print(f"CSV file '{csv_file_path}' processed and modified")

# Example usage:
gz_folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/settle/2024/aggregate/raw/daily/20240118/'
output_folder = os.path.join(gz_folder_path, 'unzipped')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all Gzip files in the folder
gz_files = glob.glob(os.path.join(gz_folder_path, '*.gz'))

# Iterate through each Gzip file and process the CSV files within
for gz_file_path in gz_files:
    process_csv_files(output_folder)
