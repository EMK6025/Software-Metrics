import os
import sqlite3

# Relative file path to the database
db_path = os.path.join('databases', '../database.db')

# Ensure the directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connect/create database
conn = sqlite3.connect(db_path)


cursor = conn.cursor()

# SQL statement to create a table
create_data_table_query = """
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    path_to_folder TEXT NOT NULL,
    path_to_file TEXT,
    user_id TEXT
);
"""

# Execute the query
cursor.execute(create_user_table_query)

# Save changes to database and close connection
conn.commit()  
conn.close()
