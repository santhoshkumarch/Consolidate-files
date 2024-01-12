import os
import pandas as pd

def compare_csv_files(folder_path):
    # Get a list of all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Check if there are at least two CSV files for comparison
    if len(csv_files) < 2:
        print("Not enough CSV files for comparison.")
        return

    # Read the first CSV file to get the header
    first_file_path = os.path.join(folder_path, csv_files[0])
    first_df = pd.read_csv(first_file_path)
    header = list(first_df.columns)

    # Iterate through the remaining CSV files and compare headers
    for csv_file in csv_files[1:]:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)

        # Compare headers
        if list(df.columns) != header:
            print(f"Headers in {csv_file} are different.")

    print("All CSV files have the same header.")

# Replace 'your_folder_path' with the actual path to your folder containing CSV files
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/xendit/bal'
compare_csv_files(folder_path)
