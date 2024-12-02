import sqlite3

# Path to your database
db_path = '../database.db'

# Connect to the database
conn = sqlite3.connect(db_path)

# Create a cursor object
cursor = conn.cursor()

# SQL query to fetch all rows from a table
query = "SELECT * FROM projects"

try:
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Close the connection
conn.close()
