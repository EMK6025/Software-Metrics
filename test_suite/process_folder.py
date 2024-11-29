import os
import subprocess
import sys

# Ensure enough arguments are passed
if len(sys.argv) != 3:
    print("Usage: python process_folder.py <dir> <metric_name>")
    sys.exit(1)

# Get the values from the command line arguments
dir = sys.argv[1]
metric_name = sys.argv[2]

dir_path = os.path.join('../projects/', sys.argv[1])
# Check if the base directory exists
if not os.path.isdir(dir_path):
    print(f"Directory not found: {dir_path}")
    sys.exit(1)

# Walk through the directory and its subdirectories
for root, _, files in os.walk(dir_path):
    for file in files:
        # Process only .java files
        if file.endswith('.java'):
            # Call process_file.py
            result = subprocess.run(
                ['python', 'process_file.py', root, file, metric_name],
                capture_output=True,
                text=True
            )
            # Output the result of the subprocess
            if result.returncode == 0:
                print(f"Processed {os.path.join(root, file)} successfully.")
            else:
                print(f"Error processing {os.path.join(root, file)}: {result.stderr}")
