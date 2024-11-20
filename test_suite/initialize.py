import sqlite3

# Relative file path to the database
db_path = '../database.db'

# Connect/create database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL statement to create a table
create_projects_table_query = """
    CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    path_to_folder TEXT NOT NULL,
    user_id TEXT
);
"""

# Execute the query
cursor.execute(create_projects_table_query)

# Save changes to database and close connection
conn.commit()  
conn.close()