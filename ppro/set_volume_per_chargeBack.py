import pandas as pd
import glob
import os

# Replace 'your_folder_path' with the actual path to your folder containing CSV files
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/settle/volume_per_chargeback/unzipped/'

# Get a list of all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

# Iterate through each CSV file
for csv_file_path in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Drop the last two rows
    # df = df[:-4]

    # Save the modified DataFrame back to a CSV file
    file_name = "modified_file.csv"
    df.to_csv(file_name, index=False)

    dfnew = pd.read_csv(file_name)

    # Check if there are rows in the DataFrame
    if not dfnew.empty:
        # Get the last row
        SETTLEMENT_DATE = dfnew.iloc[-3]


        # print("FX_FEE_RATE_PLN_USD", FX_FEE_RATE_PLN_USD)
        # print("FX_CONVERSION_RATE_PLN_USD", FX_CONVERSION_RATE_PLN_USD)
        # print("SETTLEMENT_DATE", SETTLEMENT_DATE)

        # Create a new column in the existing DataFrame with 'last_row2' as the value for the entire column
        dfnew[SETTLEMENT_DATE["MERCHANT_TX_ID"]] = SETTLEMENT_DATE["CB_ID"]
        
        # Drop the last two rows from the updated DataFrame
        dfnew = dfnew[:-3]

        # Save the updated DataFrame to the existing CSV file
        dfnew.to_csv(csv_file_path, index=False)

        print(f"New column added to the existing CSV file '{csv_file_path}'")
    else:
        print("DataFrame is empty")
