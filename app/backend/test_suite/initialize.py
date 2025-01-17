import sqlite3

# Relative file path to the database
db_path = '../database.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL statement to create a table for projects
create_projects_table_cmd = """
    CREATE TABLE IF NOT EXISTS projects
      (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    last_timestamp TEXT,
    number_of_entries INTEGER
)
"""

# Execute the query to create the projects table
cursor.execute(create_projects_table_cmd)

# Save changes to the database and close the connection
conn.commit()
conn.close()