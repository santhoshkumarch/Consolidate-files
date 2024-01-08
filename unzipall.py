import os
import gzip
import shutil

def unzip_gz_file(gz_file_path, output_file_path):
    with gzip.open(gz_file_path, 'rb') as gz_file:
        with open(output_file_path, 'wb') as output_file:
            shutil.copyfileobj(gz_file, output_file)

def unzip_all_files_in_folder(folder_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.gz'):
            gz_file_path = os.path.join(folder_path, file_name)
            output_file_path = os.path.join(output_folder, os.path.basename(gz_file_path.replace('.gz', '')))

            # Unzip the file
            unzip_gz_file(gz_file_path, output_file_path)

# Example usage:
input_folder = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/20240101/'
output_folder = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/20240101/unzipped/'

unzip_all_files_in_folder(input_folder, output_folder)
