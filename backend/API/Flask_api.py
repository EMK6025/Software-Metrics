from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

def get_db_connection():
    conn = sqlite3.connect('./database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/projects', methods=['GET'])

def get_projects():
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()
    return jsonify([dict(project) for project in projects])

def get_project_entries(proj):
    conn = get_db_connection()
    entries = conn.execute(f'SELECT * FROM {proj}').fetchall()
    conn.close()
    return jsonify([dict(entry) for entry in entries])

if __name__ == '__main__':
    app.run(debug=True)