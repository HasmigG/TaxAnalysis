from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def fetch_data():
    # Connect to SQLite database
    conn = sqlite3.connect('tax_data.db')
    cursor = conn.cursor()

    # Execute a query to select data
    select_query = """
    SELECT * FROM tax_data
    """
    cursor.execute(select_query)

    # Fetch column names
    columns = [col[0] for col in cursor.description]

    # Fetch all rows
    rows = cursor.fetchall()

    # Close connection
    conn.close()

    # Convert rows to list of dictionaries with proper labels
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))

    return data

@app.route('/')
def index():
    # Fetch data from the database
    data = fetch_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
