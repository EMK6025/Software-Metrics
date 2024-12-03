import os
import subprocess

def test_folder():
    # Fill in these
    dir_name = "sample"
    metric_name = "sample"

    # Do not touch
    dir_path = os.path.join('../projects/', dir_name)

    subprocess.run(
                    ['python', 'process_folder.py', dir_path, metric_name],
                    capture_output=True,
                    text=True
                )

def test_file():
    # Fill in these
    proj = "directory path"
    dir = "directory name"
    file = "file name"
    metric_name = "metric"

    # Do not touch
    proj_path = os.path.join('../projects/', proj)
    dir_path = os.path.join(proj_path, dir)
    subprocess.run(
                    ['python', 'process_file.py', proj_path, dir_path, file, metric_name],
                    capture_output=True,
                    text=True
                )

def update():
    subprocess.run(
                    ['python', 'update.py'],
                    capture_output=True,
                    text=True
                )



if __name__ == "__main__":
    test_folder()
    test_file()