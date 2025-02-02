import sqlite3

def get_sql_connection() -> sqlite3.Connection:
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_project_id(conn: sqlite3.Connection, author: str, repo_name: str) -> int:
    cursor = conn.cursor()
    cursor.execute("SELECT project_id FROM projects_db WHERE author = ? AND project = ?", (author, repo_name))
    result = cursor.fetchone()
    
    if result:
        return result[0] 
    else:
        cursor.execute("INSERT INTO projects_db (author, project) VALUES (?, ?)", (author, repo_name))
