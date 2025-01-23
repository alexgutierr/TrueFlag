import pandas as pd
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

# List CSV files in /data directory
csv_files = os.listdir('/data')


def load_data():
    # ETL process: loop through CSV files and load them into the OLAP database
    for csv_file in csv_files:
        if csv_file.endswith('.csv'):
            # Load CSV data
            df = pd.read_csv(f'/data/{csv_file}')

            # Generate table name based on CSV file name
            table_name = csv_file[:-4]  # Remove .csv extension

            # Load data into the database (create table if necessary)
            df.to_sql(table_name, con=engine, index=False, if_exists='replace')
            print(f"Data from {csv_file} loaded successfully into {table_name}'!.")


# Close the connection
conn.close()


if __name__ == '__main__':
    # transform_data()
    load_data()
    print("ETL process completed.")
