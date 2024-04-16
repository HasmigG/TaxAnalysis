import sqlite3
import csv
import os

# Connect to SQLite database
conn = sqlite3.connect('tax_data.db')
cursor = conn.cursor()

# Create table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS tax_data (
    year INTEGER,
    state TEXT,
    new_agi_stub INTEGER,
    Returns INTEGER,
    Single INTEGER,
    Joint INTEGER,
    Hd_of_Hshld INTEGER,
    AGI_Amt REAL,
    Std_Ded_Charity_Returns INTEGER,
    Std_Ded_Charity_Amt REAL,
    Std_Ded_Returns INTEGER,
    Std_Ded_Amt REAL,
    Itemized_Ded_Returns INTEGER,
    Itemized_Ded_Amt REAL,
    Charitable_Returns INTEGER,
    Charitable_Amt REAL
)
"""
cursor.execute(create_table_query)

# Get the file path
file_path = os.path.join('Data', 'combined_zpallagi.csv')

# Read data from CSV and insert into SQLite table
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        insert_query = """
        INSERT INTO tax_data 
        (year, state, new_agi_stub, Returns, Single, Joint, Hd_of_Hshld, AGI_Amt, Std_Ded_Charity_Returns, Std_Ded_Charity_Amt, Std_Ded_Returns, Std_Ded_Amt, Itemized_Ded_Returns, Itemized_Ded_Amt, Charitable_Returns, Charitable_Amt)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            row['year'],
            row['State'],
            row['new_agi_stub'],
            row['Returns'],
            row['Single'],
            row['Joint'],
            row['Hd_of_Hshld'],
            row['AGI_Amt'],
            row['Std_Ded_Charity_Returns'],
            row['Std_Ded_Charity_Amt'],
            row['Std_Ded_Returns'],
            row['Std_Ded_Amt'],
            row['Itemized_Ded_Returns'],
            row['Itemized_Ded_Amt'],
            row['Charitable_Returns'],
            row['Charitable_Amt']
        ))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data imported into SQLite database successfully.")
