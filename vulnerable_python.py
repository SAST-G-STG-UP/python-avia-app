
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/vulnerable')
def vulnerable():
    param = request.args.get('param')
    query = f"SELECT * FROM users WHERE username = '{param}'"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return str(cursor.fetchall())

if __name__ == "__main__":
    app.run()
