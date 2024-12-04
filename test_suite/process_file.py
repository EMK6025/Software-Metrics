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
                # Get the output value
                val = result.stdout.strip()
                # Check if the entry already exists in the table
                select_cmd = f"SELECT COUNT(*) FROM {project_name}_cur WHERE metric = ? AND file = ?"
                cursor.execute(select_cmd, (metric_name, file_name))
                count = cursor.fetchone()[0]

                if count > 0:
                    # Entry exists, then update value
                    update_cmd = f"UPDATE {project_name}_cur SET value = ? WHERE metric = ? AND file = ?"
                    cursor.execute(update_cmd, (val, metric_name, file_name))
                else:
                    # Entry does not exist, then insert a new entry
                    insert_cmd = f"INSERT INTO {project_name}_cur (metric, file, value) VALUES (?, ?, ?)"
                    cursor.execute(insert_cmd, (metric_name, file_name, val))
            except (ValueError, IOError) as e:
                print(f"Error: {e}")
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