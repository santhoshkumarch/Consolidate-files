import pandas as pd

# Read the unique header, detail, and trailer records CSV files into Pandas DataFrames
df_unique_header = pd.read_csv('unique_header_records.csv')
df_unique_detail = pd.read_csv('unique_detail_records.csv')
df_unique_trailer = pd.read_csv('unique_trailer_records.csv')

# Concatenate DataFrames along the rows axis
df_combined = pd.concat([df_unique_header, df_unique_detail, df_unique_trailer], ignore_index=True)

# Write the combined DataFrame to a new CSV file
df_combined.to_csv('combined_records.csv', index=False)

print("Combined records have been written to 'combined_records.csv'.")
