import os
import sqlite3

# Relative file path to the database
db_path = '../database.db'

# Connect/create database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

insert_cmd = "INSERT INTO projects (project_name, last_timestamp, number_of_entries) VALUES (?, ?, ?)"

check_cmd = "SELECT 1 FROM projects WHERE project_name = ? LIMIT 1"

timestamp_cmd = "SELECT CURRENT_TIMESTAMP"

for proj_name in os.listdir('../projects/'):
    folder_path = os.path.join('../projects/', proj_name)
    
    # Check if the item is a directory (not a file)
    if os.path.isdir(folder_path):
        # Check if the directory already exists in the database
        cursor.execute(check_cmd, (proj_name,))
        existing_project = cursor.fetchone()

        # If no result was found, insert the directory and create table
        if not existing_project:
            cursor.execute(timestamp_cmd)
            timestamp = cursor.fetchone()
            user_data = (proj_name, timestamp, 0)
            cursor.execute(insert_cmd, user_data)

            create_projects_table_cmd = """
                CREATE TABLE IF NOT EXISTS {dir} (
                metric TEXT NOT NULL,
                timestamp TEXT NOT NULL
                value TEXT NOT NULL,
            )
            """
            cursor.execute(create_projects_table_cmd)

            create_projects_table_cmd = """
                CREATE TABLE IF NOT EXISTS {dir}_cur (
                metric TEXT NOT NULL,
                file TEXT NOT NULL,
                value TEXT NOT NULL
            )
            """ 
# Save changes to database and close connection
conn.commit()
conn.close()