import pandas as pd
import os

def excel_to_csv(excel_file, csv_file, sheet_name):
    """
    Converts an Excel file to CSV using pandas.

    Args:
        excel_file (str): Path to the Excel file.
        csv_file (str): Path to the output CSV file.
    """

    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, skiprows=25)
        df = df.iloc[:-2]
        
        df.to_csv(csv_file, index=False)  # Prevent saving the index column
        print(f"Excel file '{excel_file}' converted to CSV '{csv_file}' successfully!")
    except Exception as e:
        print(f"Error converting Excel file: {e}")

if __name__ == "__main__":  # Entry Point of your Python Code
    current_directory = os.getcwd()  # Get the current working directory
    print("current_directory:",current_directory)
    excel_files = []

    for filename in os.listdir(current_directory):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            excel_files.append(filename)
    
    if excel_files:
        print("Excel files found in the current directory:")
        for excel_file in excel_files:
            filename = excel_file
            csv_filename = filename.replace(".xls", ".csv")
            sheet_name = "Payments"
            excel_to_csv(excel_file, csv_filename, sheet_name)
    else:
        print("No Excel files found in the current directory.")