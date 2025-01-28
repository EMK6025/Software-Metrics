import os
import importlib.util
import sys
import sqlite3

def process_file(project_id, file, date): 
    metrics_folder = "../metrics"
    db_path = '../database.db'

    for module in os.listdir(metrics_folder):
        # Importlib boilerplate to run all programs in metrics/ dynamically
        script_path = os.path.join(metrics_folder, module)
        spec = importlib.util.spec_from_file_location(module[:-3], script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.metric(file)
        try:
            # Check if the entry already exists in the table
            select_cmd = f"SELECT COUNT(*) FROM files WHERE project_id = ? AND file = ? AND metric = ? AND date = ?"
            cursor.execute(select_cmd, (project_id, file, module))
            count = cursor.fetchone()[0]
            if count > 0:
                # add customError ?
                print("files table is not supposed to have an entry")
            else:
                # Entry does not exist, then insert a new entry
                insert_cmd = f"INSERT INTO files (author, project, file, metric, value, date) VALUES (?, ?, ?, ?, ?, ?)"
                cursor.execute(insert_cmd, (project_id, file, module, result, date))
        except (ValueError, IOError) as e:
            print(f"Error: {e}")
            sys.exit()

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
