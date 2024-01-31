import os
import csv
import pandas as pd

def map_detail_record(row):
    return {
        'Transaction Currency': row[2],
        'Currency Description': row[3],
        'Merchant Funding Currency': row[4],
        'Merchant Currency Description': row[5],
        'Purchase Rate': row[6],
        'Refund Rate': row[7]
    }

def map_header_record(row):
    return {
        'Issue date': row[2],
        'Party ID': row[3],
        'Valid from': row[4],
        'Valid to': row[5],
    }

# Specify the folder path
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/311'

# Process each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith('.csv'):  # Case-insensitive file extension check
        file_path = os.path.join(folder_path, filename)

        # Read the CSV file
        try:
            with open(file_path, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)

                # Create lists to store detail records
                detail_records = [map_detail_record(row) for row in csv_reader if row[0] == '49']

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
