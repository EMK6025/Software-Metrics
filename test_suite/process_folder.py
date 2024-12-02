import os
import subprocess
import sys

def process_folder(dir_path, metric_name):
    # Check if directory exists
    if not os.path.isdir(dir_path):
        print(f"Directory not found: {dir_path}")
        return
    for root, _, files in os.walk(dir_path):
        for file in files:
            # Process only .java files
            if file.endswith('.java'):
                # Call process_file.py as a subprocess
                subprocess.run(
                    ['python', 'process_file.py', dir_path, root, file, metric_name],
                    capture_output=True,
                    text=True
                )

if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) != 3:
        print("Usage: python process_folder.py <dir> <metric_name>")
        sys.exit(1)

    # Get values from command line arguments
    dir_path = os.path.join('../projects/', sys.argv[1])
    metric_name = sys.argv[2]

    process_folder(dir_path, metric_name)
