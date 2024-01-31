import csv

def is_csv(filename):
    try:
        with open(filename, 'r') as file:
            csv.reader(file)
        return True
    except csv.Error:
        return False

# Example usage:
filename = '/Users/santhoshkumar/tazapay/Payout Recon/Sofort/txn/payment_transactions.csv'  # Replace with the actual file path
if is_csv(filename):
    print(f"{filename} is a CSV file.")
else:
    print(f"{filename} is not a CSV file.")
