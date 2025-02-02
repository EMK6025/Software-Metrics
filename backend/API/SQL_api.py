import sqlite3

def get_sql_connection() -> sqlite3.Connection:
    conn = sqlite3.connect('./database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_project_id(conn: sqlite3.Connection, author: str, repo_name: str) -> int:
    conn.execute("SELECT project_ID FROM projects WHERE author = ? and project = ?")