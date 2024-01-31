import pandas as pd

def is_header_bold(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path, nrows=1)

    # Check if the header is bold by examining the DataFrame's style
    header_style = df.style

    # Check if the font weight of the header is bold
    is_bold = 'font-weight: bold;' in header_style.to_html().split('\n')

    return is_bold

def make_header_bold(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Check if the header is bold by examining the DataFrame's style
    header_style = df.head(1).style

    # Check if the font weight of the header is bold
    is_bold = 'font-weight: bold;' in header_style.to_html().split('\n')

    # If the header is not bold, make it bold
    if not is_bold:
        new_style = header_style.set_table_styles([{'selector': 'thead th', 'props': 'font-weight: bold;'}])
        df_head_style = pd.concat([df.head(1), pd.DataFrame(columns=df.columns).style.use(new_style)])
        df = pd.concat([df_head_style, df[1:]])

        # Save the modified DataFrame back to the CSV file
        df.to_csv(csv_file_path, index=False)

csv_file_path = '/Users/santhoshkumar/tazapay/Payout Recon/Finmo/txn/report_2ff9af0d082f4575b5baa1a9ea9cd960_TRANSACTION_CSV_REPORT.csv'
make_header_bold(csv_file_path)

if is_header_bold(csv_file_path):
    print("The header is bold.")
else:
    print("The header is not bold.")
