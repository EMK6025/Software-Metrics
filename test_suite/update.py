import os
import sqlite3

# Relative file path to the database
db_path = '../database.db'

# Connect/create database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

insert_cmd = "INSERT INTO projects (project_name, path_to_folder) VALUES (?, ?)"
check_cmd = "SELECT 1 FROM projects WHERE project_name = ? LIMIT 1"

for item in os.listdir('../projects/'):
    folder_path = os.path.join('../projects/', item)
    
    # Check if the item is a directory (not a file)
    if os.path.isdir(folder_path):
        # Check if the directory already exists in the database
        cursor.execute(check_cmd, (item,))
        existing_project = cursor.fetchone()

        # If no result was found, insert the directory
        if not existing_project:
            user_data = (item, folder_path)
            cursor.execute(insert_cmd, user_data)

            # Create an empty output.txt for the new dir
            output_file_path = os.path.join(folder_path, 'output.txt')
            open(output_file_path, 'w').close()

# Save changes to database and close connection
conn.commit()
conn.close()