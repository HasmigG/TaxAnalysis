import pandas as pd
import sqlite3
from flask import Flask, jsonify

file_path = "21zpallagi.csv"
df = pd.read_csv(file_path)

# Filter relevant columns
columns_to_keep = [
    'zipcode', 'agi_stub', 'mars1', 'MARS2', 'MARS4'
]
df_filtered = df[columns_to_keep]

# Rename columns using the provided dictionary
short_column_names = {
    'zipcode': 'Zip',
    'agi_stub': 'AGI_cat',
    'mars1': 'Single',
    'MARS2': 'Joint',
    'MARS4': 'Hd_of_Hshld'
}
df_filtered.rename(columns=short_column_names, inplace=True)

# Filter out invalid ZIP codes
df_valid_zip = df_filtered[(df_filtered['Zip'] != 0) & (df_filtered['Zip'] != 99999)]

# Convert DataFrame to JSON
data_json = df_valid_zip.to_json(orient='records')

# Connect to SQLite database (optional, if you want to store the filtered data)
# conn = sqlite3.connect('data.db')
# df_valid_zip.to_sql('zip_data', conn, if_exists='replace', index=False)
# conn.close()

app = Flask(__name__)

@app.route('/zip_data')
def get_zip_data():
    return jsonify(data_json)

if __name__ == '__main__':
    app.run(debug=True)
