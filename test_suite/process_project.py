import os
import subprocess
import sys
import sqlite3


def process_folder(proj_name, metric_name):
    #path to project
    proj_path = os.path.join('../projects/', proj_name)
    # Check if directory exists
    if not os.path.isdir(proj_path):
        print(f"Directory not found: {proj_path}")
        return
    for dir_path, _, files in os.walk(proj_path):
        for file in files:
            # Process only .java files
            if file.endswith('.java'):
                # Call process_file.py as a subprocess
                subprocess.run(
                    ['python', 'process_file.py', proj_path, dir_path, file, metric_name],
                    capture_output=True,
                    text=True
                )
    timestamp_cmd = "SELECT CURRENT_TIMESTAMP"
    update_cmd = """
        UPDATE projects
        SET last_timestamp = ?
        WHERE project_name = {proj_name};
    """
    cursor.execute(timestamp_cmd)
    timestamp = cursor.fetchone()
    cursor.execute(update_cmd, timestamp)

if __name__ == "__main__":
    # Relative file path to the database
    db_path = '../database.db'

    # Connect/create database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check arguments
    if len(sys.argv) != 3:
        print("Usage: python process_folder.py <dir> <metric_name>")
        sys.exit(1)

    # Get values from command line arguments
    proj_name = sys.argv[1]
    metric_name = sys.argv[2]

    process_folder(proj_name, metric_name)
