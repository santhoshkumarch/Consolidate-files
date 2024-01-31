import os
import shutil

def extract_transaction_type(filename):
    # Extract transaction type from the filename
    parts = filename.split('_')
    
    # Check if there are enough parts
    if len(parts) >= 3:
        transaction_type = parts[2].split('.')[0]  # Extracting the part before the file extension
        return transaction_type
    else:
        return None

def consolidate_and_move(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)

        if os.path.isfile(source_path):
            # Extract transaction type from the filename
            transaction_type = extract_transaction_type(filename)

            if transaction_type:
                # Create a folder based on the transaction type
                folder_path = os.path.join(destination_directory, transaction_type)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file to the corresponding transaction type folder
                destination_path = os.path.join(folder_path, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {transaction_type}")
            else:
                print(f"Skipped {filename} - Unable to extract transaction type")

# Example usage
source_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/txn/txn_type/transaction'
destination_directory = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/txn/txn_type/transaction/consolidated_destination'
consolidate_and_move(source_directory, destination_directory)
