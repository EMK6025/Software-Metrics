import os
import subprocess
import sys
import sqlite3

def process_folder(project_name, metric_name):
    # Construct the full path to the project directory
    project_path = os.path.join('../projects/', project_name)
    project_path = os.path.normpath(project_path)

    # Check if the directory exists
    if not os.path.isdir(project_path):
        print(f"Directory not found: {project_path}")
        return

    # Iterate over all files in the project directory
    for dir_path, _, files in os.walk(project_path):
        for file in files:
            # Process only .java files
            if file.endswith('.java'):
                # Call process_file.py as a subprocess
                subprocess.run(
                    ['python', 'process_file.py', project_name, dir_path, file, metric_name],
                    capture_output=True,
                    text=True
                )

    # Get the current timestamp
    timestamp_cmd = "SELECT CURRENT_TIMESTAMP"
    cursor.execute(timestamp_cmd)
    timestamp = cursor.fetchone()[0]

    # Update the last_timestamp for the project in the projects table
    update_cmd = """
        UPDATE projects
        SET last_timestamp = ?
        WHERE project_name = ?;
    """
    cursor.execute(update_cmd, (timestamp, project_name))

if __name__ == "__main__":
    # Relative file path to the database
    db_path = '../database.db'

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check arguments
    if len(sys.argv) != 3:
        print("Usage: python process_project.py <project_name> <metric_name>")
        sys.exit(1)

    # Get values from command line arguments
    project_name = sys.argv[1]
    metric_name = sys.argv[2]

    # Call the process_folder function
    process_folder(project_name, metric_name)