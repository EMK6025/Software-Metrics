import sys
import os
import base64
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Backend.Scripts import process_update, reset
from Backend.API import Github_api, SQL_api
from datetime import datetime, timezone

def test_api(author, project):

    """
    Test the api integration.

    :param author: The author of the project to test with
    :param project: The name of the project.
    """
    git = Github_api.get_github_connection()
    conn = SQL_api.get_sql_connection()
    if Github_api.update_required(git, conn, author, project):
        print("True")

    if Github_api.update_required(git, conn, author, project):
        commits = Github_api.grab_commits(git, conn, author, project)
        file_groups = Github_api.parse_files(git, author, project, commits)
        #  process_update.main(conn, project_id, files)
        for file_group in file_groups:
            date = file_group[0]
            date_str = date.strftime('%Y-%m-%d')
            print(str(len(file_group)) + " java files modified in commits on " + date_str)
            for file in file_group[1]:
                print(file)
                decoded_file = base64.b64decode(file.content).decode('utf-8')
                print(decoded_file)
    # select_cmd = f"SELECT * FROM projects_db WHERE project_id = ?"
    # cursor = conn.cursor()
    # cursor.execute(select_cmd, (project_id))
    # print(cursor.fetchall())
    conn.close()

def print_databases():
    conn = SQL_api.get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    conn.close()

def print_table(table: str):
    conn = SQL_api.get_sql_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    print("finished")
    conn.close()

def reset_sql():
    conn = SQL_api.get_sql_connection()
    reset.reset(conn)
    conn.close()

if __name__ == "__main__":
    author = "janbodnar"
    repo = "Java-Snake-Game"
    test_api(author, repo)

    

# def test_file(proj, dir, file, metric_name):
#     """
#     Test a file by running a metric on it.

#     :param proj: The name of the project.
#     :param dir: The directory within the project.
#     :param file: The name of the file to test.
#     :param metric_name: The name of the metric to run on the file.
#     """
#     # Construct the full directory path
#     dir_path = os.path.join('../projects/', proj)
#     dir_path = os.path.join(dir_path, dir)
#     dir_path = dir_path.replace("\\", "/")

#     # Run the process_file.py script as a subprocess and capture its output
#     result = subprocess.run(
#                     ['python', 'process_file.py', proj, dir_path, file, metric_name],
#                     capture_output=True,
#                     text=True,
#                 )
#     # Print the standard output and standard error captured from the subprocess
#     print("Stdout:", result.stdout)
#     print("Stderr:", result.stderr)

# def update():
#     """
#     Update the database by running the update.py script.
#     """
#     # Run the update.py script as a subprocess and capture its output
#     result = subprocess.run(
#                     ['python', 'update.py'],
#                     capture_output=True,
#                     text=True,
#                     check=True,
#                 )
#     # Print the standard output and standard error captured from the subprocess
#     print("Stdout:", result.stdout)
#     print("Stderr:", result.stderr)

# def list_all_tables():
#     """
#     List all tables in the database.
#     """
#     # SQL command to fetch all table names in the database
#     grab_tables_cmd = "SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence'"
#     cursor.execute(grab_tables_cmd)
#     items = cursor.fetchall()
#     # Print the number of tables and their names
#     print(f"There are {len(items)} table(s): ")
#     for item in items:
#         print(item[0])

# def wipe_tables(target):
#     """
#     Wipe (drop) specified tables from the database.

#     :param target: The name of the table to drop or "all" to drop all tables.
#     """
#     # SQL command to fetch all table names in the database
#     grab_tables_cmd = "SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence'"
#     cursor.execute(grab_tables_cmd)
#     tables = cursor.fetchall()
#     # Drop each table if it matches the target or if the target is "all"
#     for table in tables:
#         if target == table[0] or target == "all":
#             wipe_cmd = f"DROP TABLE IF EXISTS {table[0]}"
#             cursor.execute(wipe_cmd)

# def display_table(table):
#     """
#     Display all rows from the specified table.

#     :param table: The name of the table to display.
#     """
#     # SQL command to fetch all rows from the specified table
#     grab_cmd = f"SELECT * FROM {table}"
#     cursor.execute(grab_cmd)
#     items = cursor.fetchall()

#     # If the table is empty, print a message saying so
#     if not items:
#         print(f"{table} is empty.")
#         return

#     # Print each row in the table
#     for item in items:
#         print("".join(str(item)))