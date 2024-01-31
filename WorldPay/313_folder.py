import csv
import os

def map_header_record(row):
    if len(row) >= 14:
        return {
            'Party Name': row[1],
            'Settlement currency': row[6],
            'Party ID': row[11],
            'Processing Date': row[13],
        }
    else:
        return None

def map_todays_record(row):
    if len(row) >= 14:
        return {
            'Today’s position': row[1],
            'Currency': row[6],
            'Amount': row[7],
            'Party ID': row[11],
            'Processing Date': row[13],
        }
    else:
        return None

# ... (similar functions for other record types)

# Function to write unique records to a CSV file
def write_unique_records(records, filename):
    if records:
        fieldnames = list(records[0].keys())
        with open(filename, 'w', newline='') as unique_file:
            csv_writer_unique = csv.DictWriter(unique_file, fieldnames=fieldnames)
            csv_writer_unique.writeheader()
            csv_writer_unique.writerows(records)

# Function to process files in a folder
def process_files_in_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.csv')]

    for csv_file in csv_files:
        unique_header_records = []
        unique_todays_records = []

        seen_header_records = set()
        seen_todays_records = set()

        csv_path = os.path.join(input_folder, csv_file)

        with open(csv_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            for row in csv_reader:
                record_type = row[0]

                if record_type == '00':
                    header_record = map_header_record(row)
                    if header_record is not None:
                        header_record_tuple = tuple(header_record.items())
                        if header_record_tuple not in seen_header_records:
                            unique_header_records.append(header_record)
                            seen_header_records.add(header_record_tuple)

                elif record_type == '01':
                    todays_record = map_todays_record(row)
                    if todays_record is not None:
                        todays_record_tuple = tuple(todays_record.items())
                        if todays_record_tuple not in seen_todays_records:
                            unique_todays_records.append(todays_record)
                            seen_todays_records.add(todays_record_tuple)

            # Write unique records for each type to separate CSV files in the output folder
            write_unique_records(unique_header_records, os.path.join(output_folder, f'unique_header_records_{csv_file}.csv'))
            write_unique_records(unique_todays_records, os.path.join(output_folder, f'unique_todays_records_{csv_file}.csv'))

# Specify the folder containing CSV files
input_csv_folder = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/313'

# Specify the output folder for unique CSV files
output_csv_folder = '/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/313'

# Call the function to process files in the input folder and write unique records to the output folder
process_files_in_folder(input_csv_folder, output_csv_folder)

print("Unique records have been written to the output folder.")
