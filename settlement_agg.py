import os
import shutil

def extract_file_purpose(filename):
    # Extract file purpose (e.g., transaction, refund, etc.) from the filename
    purposes = ["transaction", "refund", "chargeback", "aggregate"]
    for purpose in purposes:
        if purpose in filename.lower():
            return purpose
    return "other"

def consolidate_settlement_files(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)

        if os.path.isfile(source_path):
            # Extract file purpose from the filename
            file_purpose = extract_file_purpose(filename)

            if file_purpose:
                # Create a folder based on the file purpose
                folder_path = os.path.join(destination_directory, file_purpose)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file to the corresponding file purpose folder
                destination_path = os.path.join(folder_path, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {file_purpose}")
            else:
                print(f"Skipped {filename} - Unable to determine file purpose")

# Example usage
source_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/consolidated_destination/58'
destination_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/consolidated_destination/58/consolidated'
consolidate_settlement_files(source_directory, destination_directory)
