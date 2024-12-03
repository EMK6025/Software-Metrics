import os
import subprocess
import sys

def process_folder(proj_path, metric_name):
    # Check if directory exists
    if not os.path.isdir(proj_path):
        print(f"Directory not found: {proj_path}")
        return
    for dir_path, _, files in os.walk(proj_path):
        for file in files:
            # Process only .java files
            if file.endswith('.java'):
                # Call process_file.py as a subprocess
                subprocess.run(
                    ['python', 'process_file.py', proj_path, dir_path, file, metric_name],
                    capture_output=True,
                    text=True
                )

if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) != 3:
        print("Usage: python process_folder.py <dir> <metric_name>")
        sys.exit(1)

    # Get values from command line arguments
    proj_path = os.path.join('../projects/', sys.argv[1])
    metric_name = sys.argv[2]

    process_folder(proj_path, metric_name)
