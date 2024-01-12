import csv

def count_records(csv_file):
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            # Skip header if it exists
            header = next(reader, None)
            count = sum(1 for row in reader)
            return count
    except FileNotFoundError:
        return 0  # File not found
    except Exception as e:
        print(f"Error: {e}")
        return -1  # Other error

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = '/Users/santhoshkumar/tazapay/Payout Recon/PPRO/settlements/20231230/unzipped/1-478-W-2023-61-volume-per-transaction.csv'
result = count_records(csv_file_path)

if result == -1:
    print("Failed to count records.")
elif result == 0:
    print("File not found.")
else:
    print(f"Number of records in the CSV file: {result}")

