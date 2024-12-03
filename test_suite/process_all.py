import os
import subprocess

def process_all(proj_path, metric_name):
    for dir in os.listdir('../projects/'):
        dir_path = os.path.join('../projects/', dir)
        for _, _, metric in os.walk('../metrics/'):
            subprocess.run(
                        ['python', 'process_folder.py', dir_path, metric],
                        capture_output=True,
                        text=True
                    )
            
if __name__ == "__main__":
    process_all()
