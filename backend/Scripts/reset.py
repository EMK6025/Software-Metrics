import sqlite3

def reset(conn: sqlite3.Connection):
    # SQL statement to create a table for projects
    create_projects_table_cmd = """
        CREATE TABLE IF NOT EXISTS projects_db (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            project TEXT NOT NULL,
            last_update DATETIME DEFAULT '1970-01-01 00:00:00',
            number_of_entries INTEGER DEFAULT 0
        );
    """
    
    create_files_table_cmd = """
        CREATE TABLE IF NOT EXISTS files_db (
            project_id INTEGER NOT NULL,
            file_name TEXT NOT NULL,
            metric_name TEXT NOT NULL,
            value INTEGER NOT NULL,
            date DATE DEFAULT CURRENT_DATE,
            FOREIGN KEY (project_id) REFERENCES projects_db(project_id) ON DELETE CASCADE,
            UNIQUE(project_id, file_name, metric_name, date)
        );
    """
    
    create_totals_table_cmd = """
        CREATE TABLE IF NOT EXISTS totals_db (
            project_id INTEGER NOT NULL,
            metric_name TEXT NOT NULL,
            value INTEGER NOT NULL,
            date DATE NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects_db(project_id) ON DELETE CASCADE, 
            UNIQUE(project_id, metric_name, date)
        );
    """

    with conn:
        cursor = conn.cursor()

        # Execute the query to create the projects table
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("DROP TABLE IF EXISTS projects_db")
        cursor.execute("DROP TABLE IF EXISTS files_db")
        cursor.execute("DROP TABLE IF EXISTS totals_db")
        cursor.execute(create_projects_table_cmd)
        cursor.execute(create_files_table_cmd)
        cursor.execute(create_totals_table_cmd)



