import os
import subprocess
import sqlite3

def test_project():
    # Fill in these
    project_name = "single_file"
    metric_name = "boiler_plate.py"

    # Do not touch
    result = subprocess.run(
                    ['python', 'process_project.py', project_name, metric_name],
                    capture_output=True,
                    text=True,
                )
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)

def test_file():
    # Fill in these
    proj = "single_file"
    dir = ""
    file = "Calculator.java"
    metric_name = "boiler_plate.py"

    # Do not touch
    dir_path = os.path.join('../projects/', proj)
    dir_path = os.path.join(dir_path, dir)
    dir_path = dir_path.replace("\\", "/")
    result = subprocess.run(
                    ['python', 'process_file.py', proj, dir_path, file, metric_name],
                    capture_output=True,
                    text=True,
                )
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)

def update():
    result = subprocess.run(
                    ['python', 'update.py'],
                    capture_output=True,
                    text=True,
                    check=True,
                )
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)

def list_all_tables():
    grab_tables_cmd = "SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence'"
    cursor.execute(grab_tables_cmd)
    items = cursor.fetchall()
    print(f"There are {len(items)} many table(s): ")
    for item in items:
        print(item[0])

def wipe_tables():
    # Get list of all tables
    grab_tables_cmd = "SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence'"
    cursor.execute(grab_tables_cmd)
    tables = cursor.fetchall()
    # Drop each table
    for table in tables:
        wipe_cmd = f"DROP TABLE IF EXISTS {table[0]}"
        cursor.execute(wipe_cmd)

def display_table():
    table = "projects"
    grab_cmd = f"SELECT * FROM {table}"
    cursor.execute(grab_cmd)
    items = cursor.fetchall()

    if not items:
        print(f"{table} is empty.")
        return

    for item in items:
        print("".join(str(item)))
    

if __name__ == "__main__":
    db_path = '../database.db'

    # Connect/create database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    test_project()
    display_table()
    

    # Save changes to database and close connection
    conn.commit()  
    conn.close()