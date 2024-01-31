import os
import shutil

def extract_folder_name(filename):
    # Extract folder name from the filename
    parts = filename.split('-')
    
    # Check if there are enough parts
    if len(parts) >= 5:
        folder_name = parts[4].split('.')[0]  # Extracting the part before the file extension
        return folder_name
    else:
        return None

def consolidate_and_move(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)

        if os.path.isfile(source_path):
            # Extract folder name from the filename
            folder_name = extract_folder_name(filename)

            if folder_name:
                # Create a folder based on the extracted name
                folder_path = os.path.join(destination_directory, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file to the corresponding folder
                destination_path = os.path.join(folder_path, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {folder_name}")
            else:
                print(f"Skipped {filename} - Unable to extract folder name")

# Example usage
source_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements'
destination_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/consolidated_destination'
consolidate_and_move(source_directory, destination_directory)
