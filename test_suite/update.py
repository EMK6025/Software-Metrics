import os
import sqlite3

# Relative file path to the database
db_path = os.path.join('databases', '../database.db')

# Ensure the directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connect/create database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
insert_cmd = "INSERT INTO projects (project_name, path_to_folder) VALUES (?, ?)"
check_cmd = "SELECT 1 FROM projects WHERE project_name = ? LIMIT 1"

# Walk through projects/ and add new dirs in
for root, dirs in os.walk('../projects/'):
    for dir in dirs:
        # Get the full file path
        folder_path = os.path.join(root, dir)

        # Check if the directory already exists in the database
        cursor.execute(check_cmd, (dir,))
        existing_project = cursor.fetchone()

        # If no result was found, insert the directory
        if not existing_project:
            user_data = (dir, folder_path)
            cursor.execute(insert_cmd, user_data)

# Save changes to database and close connection
conn.commit()  
conn.close()