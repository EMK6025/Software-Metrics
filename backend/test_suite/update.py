import os
import sqlite3
import re

def update():
    # SQL command to insert a new project into the projects table
    insert_cmd = "INSERT INTO projects (project_name, last_timestamp, number_of_entries) VALUES (?, ?, ?)"
    # SQL command to check if a project already exists in the projects table
    check_cmd = "SELECT 1 FROM projects WHERE project_name = ? LIMIT 1"
    # SQL command to get the current timestamp
    timestamp_cmd = "SELECT CURRENT_TIMESTAMP"

    # Iterate over all directories in the projects folder
    for proj_name in os.listdir('../projects/'):
        folder_path = os.path.join('../projects/', proj_name)
        folder_path = os.path.normpath(folder_path)

        # Check if the item is a directory (not a file)
        if os.path.isdir(folder_path):
            # Validate table name to avoid SQL injection
            if not re.match(r'^[\w-]+$', proj_name):
                raise ValueError(f"Invalid directory name: {proj_name}")

            # Check if the directory already exists in the database
            cursor.execute(check_cmd, (proj_name,))
            existing_project = cursor.fetchone()

            # If no result was found, insert the directory and create tables
            if not existing_project:
                cursor.execute(timestamp_cmd)
                timestamp = cursor.fetchone()[0]  # Get the timestamp value

                user_data = (proj_name, timestamp, 0)
                cursor.execute(insert_cmd, user_data)

                # Create the table for this directory
                create_projects_table_cmd = f"""
                    CREATE TABLE IF NOT EXISTS {proj_name} (
                    metric TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    value TEXT NOT NULL
                    )
                """
                cursor.execute(create_projects_table_cmd)

                # Create the '_cur' table for this directory
                create_projects_table_cmd = f"""
                    CREATE TABLE IF NOT EXISTS {proj_name}_cur (
                    metric TEXT NOT NULL,
                    file TEXT NOT NULL,
                    value TEXT NOT NULL
                    )
                """
                cursor.execute(create_projects_table_cmd)

if __name__ == "__main__":
    # Relative file path to the database
    db_path = '../database.db'

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Call the update function
    update()

    # Save changes to the database and close the connection
    conn.commit()
    conn.close()