import sqlite3
import pandas as pd
from flask import Flask,jsonify, render_template

df = pd.read_csv('Data/combined_zpallagi.csv')

conn = sqlite3.connect('Charitable_Contributions.db')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# from Jose's app.py
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
