#latest one
import csv
import os

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
        'Issue Date': row[2],
        'Party ID': row[3],
        'Valid From': row[4],
        'Valid To': row[5]
    }

# Read the CSV file
input_filename = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/311/WP_TAZP_311FXR_20240101_001.csv'

with open(input_filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # Create a list to store combined records
    combined_records = []

    for row in csv_reader:
        record_type = row[0]

        if record_type == '49':
            combined_records.append(map_detail_record(row))
        elif record_type == '02':
            combined_records.append(map_header_record(row))

# Ensure header and detail records have consistent field names
fieldnames_combined = set(list(map_detail_record([''] * 8).keys()) + list(map_header_record([''] * 6).keys()))

# Write the combined records to the original CSV file
with open(input_filename, 'w', newline='') as combined_file:
    if combined_records:
        csv_writer_combined = csv.DictWriter(combined_file, fieldnames=fieldnames_combined)
        csv_writer_combined.writeheader()
        csv_writer_combined.writerows(combined_records)

print("Combined records have been written to the original file '{}'.".format(input_filename))
print("Current working directory:", os.getcwd())
