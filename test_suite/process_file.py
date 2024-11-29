import os
import sqlite3
import subprocess
import sys

# Ensure enough arguments are passed
if len(sys.argv) != 4:
    print("Usage: python process_file.py <dir_path> <file_name> <metric_name>")
    sys.exit(1)

# Get the values from the command line arguments
dir = sys.argv[1]
file_name = sys.argv[2]
metric_name = sys.argv[3]

# Relative file path to the database
db_path = '../database.db'

dir_path = os.path.join('../projects/', dir)
file_path = os.path.join(dir_path, file_name)
metric_path = os.path.join('../metrics/', metric_name)

# Ensure the metric file exists
if os.path.exists(metric_path):
    # Run metric
    result = subprocess.run(['python', metric_path, file_path], capture_output=True, text=True)

    if result.returncode == 0:
        try:
            # Write the output into output.txt
            metric_val = result.stdout.strip()
            output_file_path = os.path.join(dir_path, "output.txt")
            with open(output_file_path, 'w') as output_file:
                output_file.write(metric_name + " " + file_name + " " + metric_val)
        except ValueError:
            print("ValueError: script has output formatting issues.")
    else:
        print(f"Runtime error in script: {result.stderr}")
else:
    print(f"Metric script not found at {metric_path}")