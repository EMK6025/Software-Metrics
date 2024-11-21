import os
import sqlite3
import subprocess
import sys

# Ensure enough arguments are passed
if len(sys.argv) != 4:
    print("Usage: python script.py <dir_name> <file_name> <metric_name>")
    sys.exit(1)

# Get the values from the command line arguments
dir_name = sys.argv[1]
file_name = sys.argv[2]
metric_name = sys.argv[3]

# Relative file path to the database
db_path = '../database.db'

# Connect/create database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

dir_path = os.path.join('../projects/', dir_name)
file_path = os.path.join(dir_path, file_name)
metric_path = os.path.join('../metrics/', metric_name)

# Ensure the metric file exists
if os.path.exists(metric_path):
    # Run the metric by passing file_path as argument
    result = subprocess.run(['python', metric_path, file_path], capture_output=True, text=True)

    if result.returncode == 0:
        try:
            metric_value = int(result.stdout.strip())  # Convert to integer
            print(f"Metric value: {metric_value}")
        except ValueError:
            print("ValueError: script has output formatting issues.")
    else:
        print(f"Runtime error in script: {result.stderr}")
else:
    print(f"Metric script not found at {metric_path}")