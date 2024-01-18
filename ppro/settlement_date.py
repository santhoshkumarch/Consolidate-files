import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/settle/volume_per_transaction/unzipped/1-478-W-2023-46-volume-per-transaction.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Drop the last two rows
df = df[:-2]

# Save the modified DataFrame back to a CSV file
file_name = "modified_file.csv"
df.to_csv(file_name, index=False)

dfnew = pd.read_csv(file_name)

# Check if there are rows in the DataFrame
if not dfnew.empty:
    # Get the last row
    last_row = dfnew.iloc[-1]

    # Create a new column in the existing DataFrame with 'last_row2' as the value for the entire column
    dfnew[last_row["MERCHANT_TX_ID"]] = last_row["TX_ID"]

    # Drop the last two rows from the updated DataFrame
    dfnew = dfnew[:-2]

    # Save the updated DataFrame to the existing CSV file
    dfnew.to_csv(csv_file_path, index=False)

    print(f"New column added to the existing CSV file '{csv_file_path}'")
else:
    print("DataFrame is empty")
