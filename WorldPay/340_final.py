import csv
import os

def map_detail_record(row, header_info):
    return {
        'Merchant ID': row[1] if len(row) > 1 else '',
        'Merchant Outlet name': row[2] if len(row) > 2 else '',
        'Scheme Reference': row[3] if len(row) > 3 else '',
        'PAN (Card Number)': row[4] if len(row) > 4 else '',
        'Transaction Date': row[5] if len(row) > 5 else '',
        'Transaction Currency': row[6] if len(row) > 6 else '',
        'Transaction amount': row[7] if len(row) > 7 else '',
        'Payee reference (OTR)': row[8] if len(row) > 8 else '',
        'Airline ticket number': row[9] if len(row) > 9 else '',
        'Acquirer reference number': row[10] if len(row) > 10 else '',
        'Party ID': row[11] if len(row) > 11 else '',
        'Settlement Currency': row[12] if len(row) > 12 else '',
        'Store ID': row[13] if len(row) > 13 else '',
        'Fraud Type': row[14] if len(row) > 14 else '',
        'Input Method': row[15] if len(row) > 15 else '',
        'CHB Marker': row[16] if len(row) > 16 else '',
        'File Date': header_info['File Date'] if header_info and 'File Date' in header_info else '',
    }

def map_header_record(row):
    return {
        'File Date': row[1] if len(row) > 1 else '',
    }

# Specify the directory containing the CSV files
directory = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/340/'

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
        fieldnames_combined = list(map_detail_record([''] * 19, map_header_record([''] * 1)).keys())

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
