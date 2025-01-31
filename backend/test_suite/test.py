import os
import subprocess
import sqlite3
import process_update
from API import Flask_api, Github_api

def test_project(author, project):
    """
    Test a project by running a metric on it.

    :param project_name: The name of the project to test.
    :param metric_name: The name of the metric to run on the project.
    """
    git = Github_api.get_github_connection()
    conn = Flask_api.get_sql_connection()
    # FINISH later
    process_update.main()



def test_file(proj, dir, file, metric_name):
    """
    Test a file by running a metric on it.

    :param proj: The name of the project.
    :param dir: The directory within the project.
    :param file: The name of the file to test.
    :param metric_name: The name of the metric to run on the file.
    """
    # Construct the full directory path
    dir_path = os.path.join('../projects/', proj)
    dir_path = os.path.join(dir_path, dir)
    dir_path = dir_path.replace("\\", "/")

    # Run the process_file.py script as a subprocess and capture its output
    result = subprocess.run(
                    ['python', 'process_file.py', proj, dir_path, file, metric_name],
                    capture_output=True,
                    text=True,
                )
    # Print the standard output and standard error captured from the subprocess
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)

def update():
    """
    Update the database by running the update.py script.
    """
    # Run the update.py script as a subprocess and capture its output
    result = subprocess.run(
                    ['python', 'update.py'],
                    capture_output=True,
                    text=True,
                    check=True,
                )
    # Print the standard output and standard error captured from the subprocess
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)

def list_all_tables():
    """
    List all tables in the database.
    """
    # SQL command to fetch all table names in the database
    grab_tables_cmd = "SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence'"
    cursor.execute(grab_tables_cmd)
    items = cursor.fetchall()
    # Print the number of tables and their names
    print(f"There are {len(items)} table(s): ")
    for item in items:
        print(item[0])

def wipe_tables(target):
    """
    Wipe (drop) specified tables from the database.

    :param target: The name of the table to drop or "all" to drop all tables.
    """
    # SQL command to fetch all table names in the database
    grab_tables_cmd = "SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence'"
    cursor.execute(grab_tables_cmd)
    tables = cursor.fetchall()
    # Drop each table if it matches the target or if the target is "all"
    for table in tables:
        if target == table[0] or target == "all":
            wipe_cmd = f"DROP TABLE IF EXISTS {table[0]}"
            cursor.execute(wipe_cmd)

def display_table(table):
    """
    Display all rows from the specified table.

    :param table: The name of the table to display.
    """
    # SQL command to fetch all rows from the specified table
    grab_cmd = f"SELECT * FROM {table}"
    cursor.execute(grab_cmd)
    items = cursor.fetchall()

    # If the table is empty, print a message saying so
    if not items:
        print(f"{table} is empty.")
        return

    # Print each row in the table
    for item in items:
        print("".join(str(item)))

if __name__ == "__main__":
    db_path = '../database.db'

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Example usage of the functions

    # Save changes to the database and close the connection
    conn.commit()
    conn.close()