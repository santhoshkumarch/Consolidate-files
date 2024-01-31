import os
import shutil
import re

def extract_date_from_filename(filename):
    # Use regular expression to find a date pattern in the filename
    date_match = re.search(r'(\d{8})', filename)
    if date_match:
        return date_match.group(1)
    else:
        return None

def move_to_date_folders(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filename in os.listdir(source_directory):
        if filename.startswith('.'):
            print(f"Skipped {filename} - Hidden file")
            continue

        source_path = os.path.join(source_directory, filename)

        if os.path.isfile(source_path):
            # Extract date from the filename
            date_folder = extract_date_from_filename(filename)

            if date_folder:
                # Create a folder based on the date
                folder_path = os.path.join(destination_directory, date_folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file to the corresponding date folder
                destination_path = os.path.join(folder_path, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {folder_path}")
            else:
                print(f"Skipped {filename} - Unable to extract date")

# Example usage
source_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/txn/txn_type/chargeback.csv'
destination_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/txn/txn_type/chargeback.csv/consolidated'
move_to_date_folders(source_directory, destination_directory)
