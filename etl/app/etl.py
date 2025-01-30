import pandas as pd
import zipfile
from sqlalchemy import create_engine
from sqlalchemy.sql import text

import os

# Load environment variables
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Create connection string
conn_str = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Connect to PostgreSQL database
engine = create_engine(conn_str)
conn = engine.connect()

csv_files = []  # List of CSV files to load into the database


def extract_zip(zip_file_path, extract_to_folder):
    """Extract all CSV files from a ZIP archive."""
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
    print(f"Extracted {zip_file_path} to {extract_to_folder}")


def load_data(extract_folder):
    # ETL process: loop through CSV files and load them into the OLAP database
    for csv_file in csv_files:
        if csv_file.endswith('.csv'):
            # Load CSV data
            df = pd.read_csv(f'{extract_folder}/{csv_file}')

            # Generate table name based on CSV file name
            table_name = csv_file[:-4]  # Remove .csv extension

            # Load data into the database (create table if necessary)
            df.to_sql(table_name, con=engine, index=False, if_exists='replace')
            print(f"Data from {csv_file} loaded successfully into {table_name}'!.")

            try:
                # Delete the CSV file after processing
                os.remove(f'{extract_folder}/{csv_file}')
                print(f"CSV file {csv_file} deleted.")
            except Exception as e:
                print(f"Failed to delete {csv_file}: {e}")


# Close the connection
conn.close()


if __name__ == '__main__':
    print("ETL process started.")

    zip_folder = "../data"  # Folder containing ZIP files
    extract_folder = "../data/extracted"  # Folder to extract CSVs

    # Ensure the extraction folder exists
    os.makedirs(extract_folder, exist_ok=True)

    # Iterate over each ZIP file in the directory
    for file_name in os.listdir(zip_folder):
        if file_name.endswith(".zip"):
            zip_file_path = os.path.join(zip_folder, file_name)
            extract_zip(zip_file_path, extract_folder)

    # Iterate over each ZIP file in the directory
    for file_name in os.listdir(extract_folder):
        if file_name.endswith(".csv"):
            # List CSV files in /data directory
            csv_files.append(file_name)

    load_data(extract_folder)
    print("ETL process completed.")
