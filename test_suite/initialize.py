import sqlite3

# Relative file path to the database
db_path = '../database.db'

# Connect/create database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL statement to create a table
create_projects_table_cmd = """
    CREATE TABLE IF NOT EXISTS project (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    last_timestamp TEXT,
    number_of_entries INTEGER
)
"""

# Execute the query
cursor.execute(create_projects_table_cmd)

# Save changes to database and close connection
conn.commit()  
conn.close()