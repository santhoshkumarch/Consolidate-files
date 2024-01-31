import os
import csv
import pandas as pd

def map_detail_record(row):
    return {
        'Party ID': row[2],
        'Merchant ID': row[3],
        'Store Reference': row[4],
        'TID': row[5],
        'Merchant Classification Code': row[6],
        'Transaction Type': row[7],
        'Single Message OCT': row[8],
        'Settlement Party ID': row[9],
        'Issuer BIN Country': row[10],
        'PAN': row[11],
        'Card Expiry Date': row[12],
        'Transaction Amount': row[13],
        'Transaction Currency': row[14],
        'Transaction Cashback Amount': row[15],
        'Original Amount (pre DCC)': row[16],
        'Original Amount Currency (pre DCC)': row[17],
        'Acquired/processed Flag': row[18],
        'Settlement Amount': row[19],
        'Settlement Currency': row[20],
        'Transaction Date Time': row[21],
        'Pricing Segment Code': row[22],
        'Payee Reference (OTR)': row[23],
        'Acquirer Reference Number (ARN)': row[24],
        'Scheme Reference': row[25],
        'Worldpay Transaction Source': row[26],
        'Airline Ticket Number': row[27],
        'Authorisation Method': row[28],
        'Authorisation Code': row[29],
    }

# Specify the folder path
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/312'

# Process each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith('.csv'):  # Case-insensitive file extension check
        file_path = os.path.join(folder_path, filename)

        # Read the CSV file
        try:
            with open(file_path, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)

                # Create lists to store detail records
                detail_records = [map_detail_record(row) for row in csv_reader if row[0] == '01']

            # Write detail records to the same CSV file without 'Record Type' and 'Data Record Sequence Number' columns
            detail_output_path = os.path.join(folder_path, f'{filename}')
            with open(detail_output_path, 'w', newline='') as detail_file:
                fieldnames_detail = list(detail_records[0].keys())
                csv_writer_detail = csv.DictWriter(detail_file, fieldnames=fieldnames_detail)
                csv_writer_detail.writeheader()
                csv_writer_detail.writerows(detail_records)

            print(f"Detail records have been written for '{filename}'.")

        except Exception as e:
            print(f"Error processing file '{filename}': {e}")
