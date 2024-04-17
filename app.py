import sqlite3
import pandas as pd
from flask import Flask,jsonify, render_template

df = pd.read_csv('Data/combined_zpallagi.csv')
conn = sqlite3.connect('Charitable_Contributions.sqlite')
df.to_sql('tax_returns', conn, if_exists='replace', index=False)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# from Jose's app.py
@app.route('/api/v1.0/charitable_data')
def get_data():
    conn = sqlite3.connect('Charitable_Contributions.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tax_returns')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/api/v1.0/rate_of_charitable_returns')
def get_rate_of_charitable_rt():
    df = pd.read_json('Data/rate_of_charitable_returns.json')

    return df.to_dict()

if __name__ == '__main__':
    app.run(debug=True)
