from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

def get_sql_connection() -> sqlite3.Connection:
    conn = sqlite3.connect('./database.db')
    conn.row_factory = sqlite3.Row
    return conn
    
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/api/projects', methods=['GET'])

def get_projects():
    conn = get_sql_connection()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()
    return jsonify([dict(project) for project in projects])

def main():
    app.run(debug=True)