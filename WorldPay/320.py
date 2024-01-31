import os
import csv
import pandas as pd

def map_detail_record(row):
    return {
        'Activity Date': row[1],
        'Description': row[2],
        'Fee Amount': row[3],
        'Fee Currency': row[4],
        'Fee Type': row[5],
        'Invoice Number': row[6],
        'Rate': row[7],
        'Settlement Amount': row[8],
        'Settlement Currency': row[9],
        'Fee Settlement Date': row[10],
        'Tax Description': row[11],
        'Tax Indicator': row[12],
        'Tax Rate': row[13],
        'Taxable Amount': row[14],
        'Unit Fee': row[15],
        'Unit Quantity': row[16],
        'Billing Party ID': row[17],
        'Outlet Billing Party ID': row[18],
        'Payment Instruction ID': row[19],
    }

# Specify the folder path
folder_path = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/320'

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
