import os
import csv
import pandas as pd

def map_detail_record(row):
    return {
        'Transacting Party ID': row[1],
        'Merchant ID': row[2],
        'Store Reference': row[3],
        'TID': row[4],
        'Funding Party ID': row[5],
        'Batch Reference': row[6],
        'Merchant Classification Code': row[7],
        'Transaction Type': row[8],
        'Single Message OCT': row[9],
        'Issuer BIN Country': row[11],
        'PAN': row[12],
        'Card Expiry Date': row[13],
        'Transaction Amount': row[14],
        'Transaction Currency': row[15],
        'Transaction Cashback Amount': row[16],
        'Original Amount (pre DCC)': row[17],
        'Original Amount Currency (pre DCC)': row[18],
        'Acquired/processed Flag': row[19],
        'Settlement Amount': row[20],
        'Settlement Currency': row[21],
        'Transaction Date Time': row[22],
        'Pricing Segment Code': row[23],
        'Payee Reference (OTR)': row[24],
        'Acquirer Reference Number (ARN)': row[25],
        'Scheme Reference': row[26],
        'Worldpay Transaction Source': row[27],
        'Airline Ticket Number': row[28],
        'Authorisation Method': row[29],
        'Authorisation Code': row[30],
        'Trading day': row[31],
        'Premium Charge (PPT)': row[32],
        'Premium Charge (%)': row[33],
        'Transaction Charges (PPT)': row[34],
        'Transaction Charges (%)': row[35],
        'Transaction Jurisdiction': row[36],
        'Interchange Fees (Charge Currency)': row[37],
        'Scheme Fees (Charge Currency)': row[38],
        'Miscellaneous Fees (Charge Currency)': row[39],
        'Charge Currency': row[40],
        'Total Charges': row[41],
        'Invoice Number': row[42],
        'Payment Instruction ID': row[43],
    }

# Specify the folder path
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/321'

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
