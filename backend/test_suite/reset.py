import sqlite3

if __name__ == "__main__":
    # Relative file path to the database
    db_path = '../database.db'

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # SQL statement to create a table for projects
    create_projects_table_cmd = """
      CREATE TABLE IF NOT EXISTS projects
        (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT NOT NULL,
        project TEXT NOT NULL,
        last_update TEXT,
        number_of_entries INTEGER
        )
      """
    create_files_table_cmd = """
      CREATE TABLE IF NOT EXISTS files
        (
        author TEXT NOT NULL,
        project TEXT NOT NULL,
        file TEXT NOT NULL,
        metric TEXT NOT NULL,
        value
        last_update TEXT,
        number_of_entries INTEGER
        )
      """

    # Execute the query to create the projects table
    cursor.execute("DROP TABLE projects")
    cursor.execute(create_projects_table_cmd)
    cursor.execute("DROP TABLE files")
    cursor.execute(create_files_table_cmd)

    # Save changes to the database and close the connection
    conn.commit()
    conn.close()


