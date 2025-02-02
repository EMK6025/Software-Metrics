import sys
import os

# Ensure the project root (smf/) is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.test_suite import process_update
from backend.API import Github_api, SQL_api

from datetime import datetime, timezone

# def test_api(author, project, cut_off_date):
#     """
#     Test the api integration.

#     :param author: The author of the project to test with
#     :param project: The name of the project.
#     """
#     git = Github_api.get_github_connection()
#     conn = SQL_api.get_sql_connection()
#     cursor = conn.cursor()
#     project_id = SQL_api.get_project_id(conn, author, project)

#     if Github_api.update_required(git, author, project, cut_off_date):
#          commits = Github_api.grab_commits(git, author, project, cut_off_date)
#          files = Github_api.parse_files(git, author, project, commits)
#          process_update.main(conn, project_id, files)

#     select_cmd = f"SELECT * FROM projects_db WHERE project_id = ?"
#     cursor.execute(select_cmd, (project_id))
#     print(cursor.fetchall())

if __name__ == "__main__":
    # author = "EMK6025"
    # repo = "Software-Metrics"
    # cut_off_date = datetime.strptime("2025-01-15 00:00:00", "%Y-%m-%d %H:%M:%S")
    # test_api(author, repo, cut_off_date)
    print("hello world")

    

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