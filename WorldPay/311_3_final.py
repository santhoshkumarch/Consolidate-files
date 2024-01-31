import csv
import os

def map_detail_record(row, header_info):
    return {
        'Issue Date': header_info['Issue Date'],
        'Transaction Currency': row[2],
        'Currency Description': row[3],
        'Merchant Funding Currency': row[4],
        'Merchant Currency Description': row[5],
        'Purchase Rate': row[6],
        'Refund Rate': row[7],
        'Party ID': header_info['Party ID'],
        'Valid To': header_info['Valid To'],
        'Valid From': header_info['Valid From']
    }

def map_header_record(row):
    return {
        'Issue Date': row[2] if len(row) > 2 else '',
        'Party ID': row[3] if len(row) > 3 else '',
        'Valid To': row[4] if len(row) > 4 else '',
        'Valid From': row[5] if len(row) > 5 else ''
    }

# Specify the directory containing the CSV files
directory = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/311/'

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

            if record_type == '02':
                header_info = map_header_record(row)
            elif record_type == '49':
                combined_records.append(map_detail_record(row, header_info))

        # Ensure header and detail records have consistent field names
        fieldnames_combined = list(map_detail_record([''] * 8, map_header_record([''] * 4)).keys())

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
