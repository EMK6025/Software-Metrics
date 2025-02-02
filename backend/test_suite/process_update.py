import os
import importlib.util
import sqlite3
import base64
from typing import List
from ..API import SQL_api
from datetime import datetime, timezone

current_time = datetime.now()
print(current_time)  # Example output: 2025-02-02 14:30:45.123456

def main(conn: sqlite3.Connection, project_id: int, commits: List):
    select_cmd = f"SELECT COUNT(*) FROM files WHERE project_id = ? AND file = ? AND metric = ? AND date = ?"
    insert_cmd = f"INSERT INTO files (project_id, file, metric, value, date) VALUES (?, ?, ?, ?, ?)"
    update_timestamp_cmd = f"UPDATE projects SET last_update = ? WHERE project_id = ?"
    metrics_folder = "../metrics"
    cursor = conn.cursor()

    for metric_name in os.listdir(metrics_folder):
        # Importlib boilerplate to load metrics dynamically
        script_path = os.path.join(metrics_folder, metric_name)
        spec = importlib.util.spec_from_file_location(metric_name[:-3], script_path)
        metric = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(metric)

        # Run metric on each file and insert result into files table
        for files in commits:
            date = files[0]
            for file in files[1:]:
                # cache decoded result first probably, then run metrics 
                decoded_file = base64.b64decode(file.content).decode('utf-8')
                result = metric.main(decoded_file)

                try:
                    # Check if the entry already exists in the table
                    cursor.execute(select_cmd, (project_id, file, metric_name, date))
                    count = cursor.fetchone()[0]
                    if count > 0:
                        print("File already exists in the table, skipping insertion.")
                    else:
                        # Entry does not exist, insert a new entry
                        cursor.execute(insert_cmd, (project_id, file, metric_name, result, date))
                except sqlite3.Error as e:
                    print(f"SQLite error: {e}")
                    continue
                except (ValueError, IOError) as e:
                    print(f"Value/IOError: {e}")
                    continue
    date = datetime.now().replace(tzinfo=timezone.utc)
    cursor.execute(update_timestamp_cmd, (date, project_id))


