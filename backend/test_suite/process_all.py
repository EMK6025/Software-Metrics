import os
import subprocess

def process_all(proj_path, metric_name):
    # Iterate over all directories in the projects folder
    for dir in os.listdir('../projects/'):
        dir_path = os.path.join('../projects/', dir)
        dir_path = os.path.normpath(dir_path)
        # Iterate over all metrics in the metrics folder
        for _, _, metric in os.walk('../metrics/'):
            # Run the process_folder.py script as a subprocess for each metric
            subprocess.run(
                        ['python', 'process_folder.py', dir_path, metric],
                        capture_output=True,
                        text=True
                    )

if __name__ == "__main__":
    # Call the process_all function
    process_all()