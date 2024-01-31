

import pandas as pd
import os

# Function to combine unique CSV files into a single CSV file
def combine_unique_csv(input_folder, output_filename):
    # List all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.csv')]

    # Initialize an empty DataFrame to store combined data
    combined_data = pd.DataFrame()

    # Iterate over each CSV file and append its data to the combined DataFrame
    for csv_file in csv_files:
        csv_path = os.path.join(input_folder, csv_file)
        df = pd.read_csv(csv_path)
        combined_data = combined_data.append(df, ignore_index=True)

    # Write the combined DataFrame to a new CSV file
    combined_data.to_csv(output_filename, index=False)

# Specify the folder containing unique CSV files
unique_csv_folder = '/Users/santhoshkumar/tazapay/sftp-auto/WorldPay/uni'

# Specify the output filename for the combined CSV file
combined_csv_filename = '/Users/santhoshkumar/tazapay/sftp-auto/WorldPay/uni/WP_TAZP_313PRC_V03_20240102_001.csv'

# Call the function to combine unique CSV files into a single CSV file
combine_unique_csv(unique_csv_folder, combined_csv_filename)

print(f"Combined unique records have been written to '{combined_csv_filename}'.")
