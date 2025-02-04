import sqlite3
from datetime import datetime, timezone

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
        return add_project(conn, author, repo_name)


def get_project_update(conn: sqlite3.Connection, author: str, repo_name: str) -> str:
    cursor = conn.cursor()
    cursor.execute("SELECT last_update FROM projects_db WHERE author = ? AND project = ?", (author, repo_name))
    result = cursor.fetchone()
    
    if result:
        return datetime.strptime(result[0] , '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc) # Strip datetime and add UTC timezone
    
    else:
        add_project(conn, author, repo_name)
        return "1970-01-01 00:00:00"


def add_project(conn: sqlite3.Connection, author: str, repo_name: str) -> int:
    try:
        insert_cmd = f"INSERT INTO projects_db (author, project) VALUES (?, ?)"
        with conn:
            cursor = conn.cursor()
            cursor.execute(insert_cmd, (author, repo_name))
            return cursor.lastrowid
    except sqlite3.IntegrityError:  # Handles duplicate entries, foreign key violations, etc.
        print(f"Failed to insert project '{repo_name}' for author '{author}': Integrity Error")
        return -1
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return -1
