import csv
import os

def map_detail_record(row, header_info):
    return {
        'Party ID': row[1] if len(row) > 1 else '',
        'Merchant ID': row[2] if len(row) > 2 else '',
        'Store Reference': row[3] if len(row) > 3 else '',
        'TID': row[4] if len(row) > 4 else '',
        'Merchant Classification Code': row[5] if len(row) > 5 else '',
        'Transaction Type': row[6] if len(row) > 6 else '',
        'Single Message OCT': row[7] if len(row) > 7 else '',
        'Settlement Party ID': row[8] if len(row) > 8 else '',
        'Issuer BIN Country': row[9] if len(row) > 9 else '',
        'PAN': row[10] if len(row) > 10 else '',
        'Card Expiry Date': row[11] if len(row) > 11 else '',
        'Transaction Amount': row[12] if len(row) > 12 else '',
        'Transaction Currency': row[13] if len(row) > 13 else '',
        'Transaction Cashback Amount': row[14] if len(row) > 14 else '',
        'Original Amount (pre DCC)': row[15] if len(row) > 15 else '',
        'Original Amount Currency (pre DCC)': row[16] if len(row) > 16 else '',
        'Acquired/processed Flag': row[17] if len(row) > 17 else '',
        'Settlement Amount': row[18] if len(row) > 18 else '',
        'Settlement Currency': row[19] if len(row) > 19 else '',
        'Transaction Date Time': row[20] if len(row) > 20 else '',
        'Pricing Segment Code': row[21] if len(row) > 21 else '',
        'Payee Reference (OTR)': row[22] if len(row) > 22 else '',
        'Acquirer Reference Number (ARN)': row[23] if len(row) > 23 else '',
        'Scheme Reference': row[24] if len(row) > 24 else '',
        'Worldpay Transaction Source': row[25] if len(row) > 25 else '',
        'Airline Ticket Number': row[26] if len(row) > 26 else '',
        'Authorisation Method': row[27] if len(row) > 27 else '',
        'Authorisation Code': row[28] if len(row) > 28 else '',
        'Trading day': row[29] if len(row) > 29 else '',
        'Data File Date': header_info['Data File Date'],
    }

def map_header_record(row):
    return {
        'Data File Date': row[1] if len(row) > 1 else '',
    }

# Specify the directory containing the CSV files
directory = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/312/'

# List all files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.CSV')]

# Process each CSV file
for csv_file in csv_files:
    input_filename = os.path.join(directory, csv_file)

    with open(input_filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Create a list to store combined records
        combined_records = []
        header_info = None

        for row in csv_reader:
            record_type = row[0]

            if record_type == '00':
                header_info = map_header_record(row)
            elif record_type == '01':
                combined_records.append(map_detail_record(row, header_info))

        # Ensure header and detail records have consistent field names
        fieldnames_combined = list(map_detail_record([''] * 27, map_header_record([''] * 1)).keys())

        # Write the combined records to a new CSV file
        output_filename = os.path.join(directory, 'combined_' + csv_file)
        with open(output_filename, 'w', newline='') as combined_file:
            if combined_records:
                csv_writer_combined = csv.DictWriter(combined_file, fieldnames=fieldnames_combined)
                csv_writer_combined.writeheader()
                csv_writer_combined.writerows(combined_records)

        print("Combined records have been written to the new file '{}'.".format(output_filename))

print("Processing complete for all CSV files in the directory.")
print("Current working directory:", os.getcwd())
