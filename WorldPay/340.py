import os
import csv
import pandas as pd

def map_detail_record(row):
    return {
        'Merchant ID': row[1],
        'Merchant Outlet name': row[2],
        'Scheme Reference': row[3],
        'PAN (Card Number)': row[4],
        'Transaction Date': row[5],
        'Transaction Currency': row[6],
        'Transaction amount': row[7],
        'Payee reference (OTR)': row[8],
        'Airline ticket number': row[9],
        'Acquirer reference number': row[10],
        'Party ID': row[11],
        'Settlement Currency': row[12],
        'Store ID': row[13],
        'Fraud Type': row[14],
        'Input Method': row[15],
        'CHB Marker': row[16],
    }

# Specify the folder path
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/340'

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
