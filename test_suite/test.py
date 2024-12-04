import os
import subprocess
import sqlite3

def test_folder():
    # Fill in these
    dir_name = "sample"
    metric_name = "sample"

    # Do not touch
    dir_path = os.path.join('../projects/', dir_name)

    subprocess.run(
                    ['python', 'process_folder.py', dir_path, metric_name],
                    capture_output=True,
                    text=True
                )

def test_file():
    # Fill in these
    proj = "directory path"
    dir = "directory name"
    file = "file name"
    metric_name = "metric"

    # Do not touch
    proj_path = os.path.join('../projects/', proj)
    dir_path = os.path.join(proj_path, dir)
    subprocess.run(
                    ['python', 'process_file.py', proj_path, dir_path, file, metric_name],
                    capture_output=True,
                    text=True
                )

def update():
    subprocess.run(
                    ['python', 'update.py'],
                    capture_output=True,
                    text=True
                )

def display_tables():
    grab_tables_cmd = """
        SELECT name 
        FROM sqlite_master 
        WHERE type = 'table' AND name != 'sqlite_sequence';
    """
    cursor.execute(grab_tables_cmd)
    items = cursor.fetchall()
    print(f"There are {len(items)} many table(s): ")
    for item in items:
        print(item[0])

def wipe_tables():
    # Get a list of all tables
    wipe_cmd = "SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence'"
    cursor.execute(wipe_cmd)
    tables = cursor.fetchall()

    # Drop each table
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")



if __name__ == "__main__":
    db_path = '../database.db'

    # Connect/create database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # test_folder()
    # test_file()
    display_tables()

    # Save changes to database and close connection
    conn.commit()  
    conn.close()