import os
import shutil

# Directory where your files are located
source_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/settle'

# List of files in the source directory
files = [f for f in os.listdir(source_directory) if not f.startswith('.')]

# Keywords to identify the description in the filenames
keywords = ['aggregate', 'fee-per-chargeback', 'fee-per-refund', 'fee-per-transaction', 'volume-per-chargeback', 'volume-per-refund', 'volume-per-transaction']

# Iterate through files and move/copy them to appropriate directories
for file in files:
    filename, file_extension = os.path.splitext(file)
    
    # Find the keyword present in the filename
    description = next((kw for kw in keywords if kw in filename), None)

    # Create a new directory based on the description if it is found
    if description:
        output_directory = os.path.join(source_directory, description)
        os.makedirs(output_directory, exist_ok=True)

        # Construct the full paths
        source_path = os.path.join(source_directory, file)
        destination_path = os.path.join(output_directory, file)

        # Check if source and destination paths are different
        if source_path != destination_path:
            # Print the paths for debugging
            print(f"Moving {source_path} to {destination_path}")

            # Move or copy the file to the appropriate directory
            shutil.move(source_path, destination_path)
            # If you want to copy instead of move, use shutil.copy

print("Files have been separated based on their descriptions in the source folder.")
