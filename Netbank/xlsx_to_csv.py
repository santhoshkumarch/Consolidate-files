import os
import pandas as pd

# Replace 'path/to/transaction/files' with the path to your transaction files folder
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/Netbank/transaction file/'

# Loop through all files in the folder and its subfolders
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith('.xlsx'):
            # Construct the full file path
            file_path = os.path.join(root, filename)

            # Load the Excel file into a pandas DataFrame
            df = pd.read_excel(file_path, header=None)

            # Remove the first 10 rows and last 2 rows
            df = df.iloc[9:-2]

            # Set the third row as the new header
            df.columns = df.iloc[1]
            df = df[2:]

            # Construct the output CSV file path in the same subfolder structure
            relative_path = os.path.relpath(file_path, folder_path)
            csv_file = os.path.join(folder_path, f'{os.path.splitext(relative_path)[0]}_processed.csv')

            # Save the DataFrame to a CSV file
            df.to_csv(csv_file, index=False)

            print(f'{file_path} has been processed and saved to {csv_file}')
