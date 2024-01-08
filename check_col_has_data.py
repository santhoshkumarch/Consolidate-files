import os
import pandas as pd

def are_columns_empty(csv_file, columns_to_check):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Check if all specified columns are present in the DataFrame
        missing_columns = [col for col in columns_to_check if col not in df.columns]
        if missing_columns:
            print(f"Columns {missing_columns} not found in the CSV file '{csv_file}'.")
            return False

        # Check if any value in the specified columns is not null
        are_empty = df[columns_to_check].notna().all().all()

        if are_empty:
            print(f"All columns {columns_to_check} in '{csv_file}' are empty.")
        else:
            print(f"At least one column in {columns_to_check} in '{csv_file}' has data.")

        return are_empty

    except Exception as e:
        print(f"An error occurred while processing '{csv_file}': {e}")
        return False

def check_all_files(folder_path, columns_to_check):
    # List all files in the specified folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    for file in files:
        file_path = os.path.join(folder_path, file)
        print(f"\nChecking file: {file}")
        are_empty = are_columns_empty(file_path, columns_to_check)

# Example usage
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/settle/volume_per_transaction/unzipped/'
columns_to_check = ['CURRENCY', 'AMOUNT']

check_all_files(folder_path, columns_to_check)
