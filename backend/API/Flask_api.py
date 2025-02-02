from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import SQL_api

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/api/projects', methods=['GET'])

def get_projects():
    conn = SQL_api.get_sql_connection()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()
    return jsonify([dict(project) for project in projects])

def main():
    app.run(debug=True)