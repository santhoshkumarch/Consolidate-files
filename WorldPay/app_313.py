import pandas as pd
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

def map_balancing_item_record(row):
    if len(row) >= 14:
        return {
            'Balance carried forward': row[1],
            'Payment instruction ID': row[3],
            'Currency': row[6],
            'Amount': row[7],
            'Party ID': row[11],
            'Due date': row[12],
            'Processing date': row[13],
        }
    else:
        return None
    
def map_final_settlement_record(row):
    if len(row) >= 14:
        return {
            'Settlement amount': row[1],
            'Currency': row[6],
            'Amount': row[7],
            'Party ID': row[11],
            'Processing date': row[13],
        }
    else:
        return None
    
def map_ind_entry_record(row):
    if len(row) >= 14:
        return {
            'Description': row[1],
            'Payment instruction ID': row[3],
            'Currency': row[6],
            'Amount': row[7],
            'Party ID': row[11],
            'Due date': row[12],
            'Processing date': row[13],
        }
    else:
        return None
    
def map_total_funding_record(row):
    if len(row) >= 14:
        return {
            'Acquired Cards Subtotal': row[1],
            'Funding Bill ID': row[2],
            'Payment instruction ID': row[3],
            'Number of transactions': row[5],
            'Currency': row[6],
            'Value of Transactions': row[7],
            'Party ID': row[11],
            'Processing date': row[13],

        }
    else:
        return None
    
def map_txn_charges_records(row):
    if len(row) >= 14:
        return {
            'Acquired charges Subtotal': row[1],
            'Bill ID': row[2],
            'Payment instruction ID': row[3],
            'Number of transactions': row[5],
            'Currency': row[6],
            'Value of transactions':row[7],
            'Party ID': row[11],
            'Processing date': row[13],
        }
    else:
        return None
    
def map_total_miscellaneous_charges_records(row):
    if len(row) >= 14:
        return {
            'Miscellaneous charges': row[1],
            'Bill ID': row[2],
            'Payment instruction ID': row[3],
            'Number of transactions': row[5],
            'Currency': row[6],
            'Value of transactions': row[7],
            'Party ID': row[11],
            'Processing date': row[13],
        }
    else:
        return None

def map_total_tax_applied_records(row):
    if len(row) >= 14:
        return {
            'TAX': row[1],
            'Bill ID': row[2],
            'Payment instruction ID': row[3],
            'Currency': row[6],
            'Tax applied': row[7],
            'Party ID': row[11],
            'Processing date': row[13],
        }
    else:
        return None


# Read the CSV file and find unique records for each type
unique_header_records = []
unique_todays_records = []
unique_balancing_records = []
unique_final_settlement_records = []
unique_ind_entry_records = []
unique_total_funding_records = []
unique_txn_charges_records = []
unique_total_miscellaneous_charges_records = []
unique_total_tax_applied_records = []

seen_header_records = set()
seen_todays_records = set()
seen_balancing_records = set()
seen_final_settlement_records = set()
seen_ind_entry_records = set()
seen_total_funding_records = set()
seen_txn_charges_records = set()
seen_total_miscellaneous_charges_records = set()
seen_total_tax_applied_records = set()


with open('/Users/santhoshkumar/tazapay/Payout Recon/Worldpay/313/WP_TAZP_313PRC_V03_20240102_001.csv', 'r') as csvfile:
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
            detail_record = map_todays_record(row)
            if detail_record is not None:
                detail_record_tuple = tuple(detail_record.items())
                if detail_record_tuple not in seen_todays_records:
                    unique_todays_records.append(detail_record)
                    seen_todays_records.add(detail_record_tuple)
        
        elif record_type == '02':
            balancing_record = map_balancing_item_record(row)
            if balancing_record is not None:
                balancing_record_tuple = tuple(balancing_record.items())
                if balancing_record_tuple not in seen_balancing_records:
                    unique_balancing_records.append(balancing_record)
                    seen_balancing_records.add(balancing_record_tuple)
        
        elif record_type == '03':
            final_settlement_record = map_final_settlement_record(row)
            if final_settlement_record is not None:
                final_settlement_record_tuple = tuple(final_settlement_record.items())
                if final_settlement_record_tuple not in seen_final_settlement_records:
                    unique_final_settlement_records.append(final_settlement_record)
                    seen_final_settlement_records.add(final_settlement_record_tuple)
        
        elif record_type == '04':
            ind_entry_record = map_ind_entry_record(row)
            if ind_entry_record is not None:
                ind_entry_record_tuple = tuple(ind_entry_record.items())
                if ind_entry_record_tuple not in seen_ind_entry_records:
                    unique_ind_entry_records.append(ind_entry_record)
                    seen_ind_entry_records.add(ind_entry_record_tuple)

        elif record_type == '05':
            total_funding_record = map_total_funding_record(row)
            if total_funding_record is not None:
                total_funding_record_tuple = tuple(total_funding_record.items())
                if total_funding_record_tuple not in seen_total_funding_records:
                    unique_total_funding_records.append(total_funding_record)
                    seen_total_funding_records.add(total_funding_record_tuple)
        
        elif record_type == '08':
            txn_charges_record = map_txn_charges_records(row)
            if txn_charges_record is not None:
                txn_charges_record_tuple = tuple(txn_charges_record.items())
                if txn_charges_record_tuple not in seen_txn_charges_records:
                    unique_txn_charges_records.append(txn_charges_record)
                    seen_txn_charges_records.add(txn_charges_record_tuple)

        elif record_type == '12':
            total_miscellaneous_charges_record = map_total_miscellaneous_charges_records(row)
            if total_miscellaneous_charges_record is not None:
                total_miscellaneous_charges_record_tuple = tuple(total_miscellaneous_charges_record.items())
                if total_miscellaneous_charges_record_tuple not in seen_total_miscellaneous_charges_records:
                    unique_total_miscellaneous_charges_records.append(total_miscellaneous_charges_record)
                    seen_total_miscellaneous_charges_records.add(total_miscellaneous_charges_record_tuple)

        elif record_type == '14':
            total_tax_applied_record = map_total_tax_applied_records(row)
            if total_tax_applied_record is not None:
                total_tax_applied_record_tuple = tuple(total_tax_applied_record.items())
                if total_tax_applied_record_tuple not in seen_total_tax_applied_records:
                    unique_total_tax_applied_records.append(total_tax_applied_record)
                    seen_total_tax_applied_records.add(total_tax_applied_record_tuple)

# Write unique records for each type to separate CSV files
def write_unique_records(records, filename):
    if records:
        fieldnames = list(records[0].keys())
        with open(filename, 'w', newline='') as unique_file:
            csv_writer_unique = csv.DictWriter(unique_file, fieldnames=fieldnames)
            csv_writer_unique.writeheader()
            csv_writer_unique.writerows(records)

write_unique_records(unique_header_records, 'unique_header_records.csv')
write_unique_records(unique_todays_records, 'unique_todays_records.csv')
write_unique_records(unique_balancing_records, 'unique_balancing_records.csv')
write_unique_records(unique_final_settlement_records, 'unique_final_settlement_records.csv')
write_unique_records(unique_ind_entry_records, 'unique_ind_entry_records.csv')
write_unique_records(unique_total_funding_records, 'unique_total_funding_records.csv')
write_unique_records(unique_txn_charges_records, 'unique_txn_charges_records.csv')
write_unique_records(unique_total_miscellaneous_charges_records, 'unique_total_miscellaneous_charges_records.csv')
write_unique_records(unique_total_tax_applied_records, 'unique_total_tax_applied_records.csv')

print("Unique header, detail, and trailer records have been written to 'unique_header_records.csv', 'unique_detail_records.csv', and 'unique_trailer_records.csv'.")