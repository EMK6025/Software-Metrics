import os
import subprocess
import sys
import sqlite3

def process_file(project_name, project_dir, file_name, metric_name):
    file_path = os.path.join(project_dir, file_name)
    file_path = file_path.replace("\\", "/")
    metric_path = os.path.join('../metrics/', metric_name)
    metric_path = metric_path.replace("\\", "/")
    # Ensure the metric file exists
    if os.path.exists(metric_path):
        # Run metric
        result = subprocess.run(['python', metric_path, file_path], capture_output=True, text=True)

        if result.returncode == 0:
            try:
                # Write the output into cur table for project
                val = result.stdout.strip()
                insert_cmd = f"INSERT INTO {project_name}_cur (metric, file, value) VALUES (?, ?, ?)"
                print("completed")
                sql_data = (metric_name, file_name, val)
                cursor.execute(insert_cmd, sql_data)
            except ValueError:
                sys.exit()
            except IOError:
                sys.exit()


if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) != 5:
        print("Usage: python process_file.py <project_name> <project_dir> <file_name> <metric_name>")
        sys.exit(1)

    # Get values from command line arguments
    project_name = sys.argv[1]
    project_dir = sys.argv[2]
    file_name = sys.argv[3]
    metric_name = sys.argv[4]

    # Relative file path to the database
    db_path = '../database.db'

    # Connect/create database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    process_file(project_name, project_dir, file_name, metric_name)
    conn.commit()  
    conn.close()