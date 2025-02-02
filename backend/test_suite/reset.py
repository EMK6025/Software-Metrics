import sqlite3

if __name__ == "__main__":
    


# Relative file path to the database
    db_path = '../database.db'

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # SQL statement to create a table for projects
    create_projects_table_cmd = """
        CREATE TABLE IF NOT EXISTS projects_db (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            project TEXT NOT NULL,
            last_update DATETIME,
            number_of_entries INTEGER
        );
    """
    
    create_files_table_cmd = """
        CREATE TABLE IF NOT EXISTS files_db (
            project_id INTEGER NOT NULL,
            file_name TEXT NOT NULL,
            metric_name TEXT NOT NULL,
            value INTEGER NOT NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects_db(project_id) ON DELETE CASCADE,
            UNIQUE(project_id, file_name, metric_name, date)
        );
    """
    
    create_totals_table_cmd = """
        CREATE TABLE IF NOT EXISTS totals_db (
            project_id INTEGER NOT NULL,
            metric_name TEXT NOT NULL,
            value INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE, 
            UNIQUE(project_id, metric_name, date)
        );
    """
    # Execute the query to create the projects table
    cursor.execute("DROP TABLE IF EXISTS projects_db")
    cursor.execute(create_projects_table_cmd)
    cursor.execute("DROP TABLE IF EXISTS files_db")
    cursor.execute(create_files_table_cmd)
    cursor.execute("DROP TABLE IF EXISTS totals_db")
    cursor.execute(create_totals_table_cmd)

    # Save changes to the database and close the connection
    conn.commit()
    conn.close()


