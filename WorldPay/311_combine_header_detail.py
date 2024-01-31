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
with open('/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/311/WP_TAZP_311FXR_20231114_001.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # Create lists and a dictionary to store detail, header, and trailer records
    detail_records = []
    header_records_dict = {}  # Using a dictionary to handle duplicates
    trailer_records = []

    for row in csv_reader:
        record_type = row[0]

        if record_type == '49':
            detail_records.append(map_detail_record(row))
        elif record_type == '02':
            # Use the 'Party ID' as a unique identifier for header records
            party_id = row[3]
            
            # Check if the party_id already exists in the dictionary
            if party_id not in header_records_dict:
                header_records_dict[party_id] = map_header_record(row)

# Convert the header dictionary values to a list
header_records = list(header_records_dict.values())

# Write header records to a single CSV file
with open('header_records.csv', 'w', newline='') as header_file:
    if header_records:
        fieldnames_header = list(header_records[0].keys())
        csv_writer_header = csv.DictWriter(header_file, fieldnames=fieldnames_header)
        csv_writer_header.writeheader()
        csv_writer_header.writerows(header_records)

# Write detail records to a single CSV file without 'Record Type' and 'Data Record Sequence Number' columns
with open('detail_records.csv', 'w', newline='') as detail_file:
    if detail_records:
        fieldnames_detail = list(detail_records[0].keys())
        csv_writer_detail = csv.DictWriter(detail_file, fieldnames=fieldnames_detail)
        csv_writer_detail.writeheader()
        csv_writer_detail.writerows(detail_records)

# Ensure detail and header records have consistent field names
fieldnames_combined = set(fieldnames_detail).union(fieldnames_header)

# Combine the detail and header records
combined_records = header_records + detail_records

# Write the combined records to a single CSV file
combined_csv_filename = 'combined_records.csv'
with open(combined_csv_filename, 'w', newline='') as combined_file:
    if combined_records:
        csv_writer_combined = csv.DictWriter(combined_file, fieldnames=fieldnames_combined)
        csv_writer_combined.writeheader()
        csv_writer_combined.writerows(combined_records)

print("Combined records have been written to '{}'.".format(combined_csv_filename))
print("Current working directory:", os.getcwd())
