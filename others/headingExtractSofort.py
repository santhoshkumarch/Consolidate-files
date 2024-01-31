import csv
import os

def get_table_heading(csv_file_path):
    with open(csv_file_path, 'r', encoding='latin-1') as file:
        # Specify the delimiter as a semicolon
        reader = csv.reader(file, delimiter=';')
        # Assuming the first row contains the column names
        column_names = next(reader)

    data_types = ["string"] * len(column_names)  # You may customize this based on your data

    table_heading = generate_table_heading(column_names, data_types)
    return table_heading

def generate_table_heading(column_names, data_types):
    table_heading = []

    for col_name, data_type in zip(column_names, data_types):
        table_heading.append((col_name, data_type, col_name, data_type))

    return table_heading

def write_to_text_file(output, output_file_path):
    directory = os.path.dirname(output_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(output_file_path, 'w') as file:
        for entry in output:
            file.write(str(entry) + ",\n")

csv_file_path = '/Users/santhoshkumar/tazapay/Payout Recon/Standard Chartered bank (SCB)/Disbursement file/ExportPymt.csv'
output_file_path = '/Users/santhoshkumar/tazapay/Payout Recon/Standard Chartered bank (SCB)/Disbursement file/output.txt'  # Replace with the desired output file path

result = get_table_heading(csv_file_path)
write_to_text_file(result, output_file_path)
