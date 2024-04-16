import pandas as pd
import sqlite3
from flask import Flask, jsonify



file_path = "21zpallagi.csv"
df = pd.read_csv(file_path)
df.head()
columns_to_keep = [
    'STATE', 'zipcode', 'agi_stub', 'N1', 'mars1', 'MARS2', 
    "MARS4"
    ,'A00100', 'A02650', 'N01000', 'A01000', 'N02910', 'A02910',
    'N04470', 'A04470', 'N17000', 'A17000', 'N18300', 'A18300',
    'N19700', 'A19700', 'N20950', 'A20950', 'N85775', 'A85300'
]

df_filtered = df[columns_to_keep]
df_filtered
df_AL = df_filtered.loc[df_filtered['STATE'] == "AL"]
df_AL
# Dictionary mapping original column names to shorter names
short_column_names = {
    'STATE': 'State',
    'zipcode': 'Zip',
    'agi_stub': 'AGI_cat',
    'N1': 'Returns',
    'mars1': 'Single',
    'MARS2': 'Joint',
    'MARS4': 'Hd_of_Hshld',
    'A00100': 'AGI',
    'A02650': 'Total_Income',
    'N01000': 'Cap_Gain_Returns',
    'A01000': 'Cap_Gain_Amt',
    'N02910': 'Std_Ded_Charity_Returns',
    'A02910': 'Std_Ded_Charity_Amt',
    'N04470': 'Itemized_Ded_Returns',
    'A04470': 'Itemized_Ded_Amt',
    'N17000': 'Med_Dental_Returns',
    'A17000': 'Med_Dental_Amt',
    'N18300': 'Total_Taxes_Returns',
    'A18300': 'Total_Taxes_Amt',
    'N19700': 'Charitable_Returns',
    'A19700': 'Charitable_Amt',
    'N20950': 'Misc_Ded_Returns',
    'A20950': 'Misc_Ded_Amt',
    'N85775': 'Advance_Premium_Returns',
    'A85300': 'Net_Investment_Tax_Amt'
}

# Rename columns
df_short_names = df_AL.rename(columns=short_column_names)

# Now df_short_names contains columns with shorter names
df_short_names
df_AL_valid_zip = df_short_names[(df_short_names['Zip'] != 0) & (df_short_names['Zip'] != 99999)]

# Display the filtered DataFrame
df_AL_valid_zip
# Sum up all the columns in the 'Returns' row
returns_sum = df_AL_valid_zip.loc[:, 'Returns'].sum()
single_sum = df_AL_valid_zip.loc[:, 'Single'].sum()
joit_sum = df_AL_valid_zip.loc[:, 'Joint'].sum()
hd_of_Hshld_sum = df_AL_valid_zip.loc[:, 'Hd_of_Hshld'].sum()
# Display the sum
print("Total Returns:", returns_sum)
print("Total Single:", single_sum)
print("Total Joint:", joit_sum)
print("Total Head of Household:", hd_of_Hshld_sum)
# Calculate percentages
single_percentage = (single_sum / returns_sum) * 100
joint_percentage = (joit_sum / returns_sum) * 100
hd_of_hshld_percentage = (hd_of_Hshld_sum / returns_sum) * 100

# Display the percentages
print("Percentage of Returns that are Single:", single_percentage)
print("Percentage of Returns that are Joint:", joint_percentage)
print("Percentage of Returns that are Head of Household:", hd_of_hshld_percentage)


# Connect to SQLite database
conn = sqlite3.connect('data.db')

# Store DataFrame in SQLite database
df_AL_valid_zip.to_sql('zip_data', conn, if_exists='replace', index=False)

# Close connection
conn.close()

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/zip_data')
def get_zip_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM zip_data')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
