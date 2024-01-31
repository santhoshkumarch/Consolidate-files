import csv
import os

def map_detail_record(row, header_info):
    return {
        'Activity Date': row[1] if len(row) > 1 else '',
        'Description': row[2] if len(row) > 2 else '',
        'Fee Amount': row[3] if len(row) > 3 else '',
        'Fee Currency': row[4] if len(row) > 4 else '',
        'Fee Type': row[5] if len(row) > 5 else '',
        'Invoice Number': row[6] if len(row) > 6 else '',
        'Rate': row[7] if len(row) > 7 else '',
        'Settlement Amount': row[8] if len(row) > 8 else '',
        'Settlement Currency': row[9] if len(row) > 9 else '',
        'Fee Settlement Date': row[10] if len(row) > 10 else '',
        'Tax Description': row[11] if len(row) > 11 else '',
        'Tax Indicator': row[12] if len(row) > 12 else '',
        'Tax Rate': row[13] if len(row) > 13 else '',
        'Taxable Amount': row[14] if len(row) > 14 else '',
        'Unit Fee': row[15] if len(row) > 15 else '',
        'Unit Quantity': row[16] if len(row) > 16 else '',
        'Billing Party ID': row[17] if len(row) > 17 else '',
        'Outlet Billing Party ID': row[18] if len(row) > 18 else '',
        'Payment Instruction ID': row[19] if len(row) > 19 else '',
        'File Date': header_info['File Date'] if header_info and 'File Date' in header_info else '',
    }

def map_header_record(row):
    return {
        'File Date': row[1] if len(row) > 1 else '',
    }

# Specify the directory containing the CSV files
directory = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/320/'

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
