import os
import csv

def clean_csv(input_file_path):
    """
    Cleans a CSV file by removing commas from cells and replacing backslashes with forward slashes.

    Args:
    - input_file_path (str): Path to the input CSV file.
    """
    # Ensure the file has '.csv' extension, and if not, add it
    if not input_file_path.endswith('.csv'):
        input_file_path += '.csv'

    # Read data from the input CSV file
    with open(input_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]

    # Clean the data by removing commas and replacing backslashes
    cleaned_data = []
    for row in data:
        cleaned_row = [cell.replace(',', '').replace("\\", "/") for cell in row]
        cleaned_data.append(cleaned_row)

    # Generate the output file name with "_clean" appended
    output_file_path = input_file_path.replace('.csv', '_clean.csv')

    # Write the cleaned data to the output CSV file
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(cleaned_data)

# Specify the folder containing the CSV files (relative path)
folder_path = 'final_path_here'

# Get the current working directory
script_path = os.getcwd()
full_folder_path = os.path.join(script_path, folder_path)

# Iterate through all files in the folder
for filename in os.listdir(full_folder_path):
    if filename.endswith('.csv'):
        full_path = os.path.join(full_folder_path, filename)
        clean_csv(full_path)
