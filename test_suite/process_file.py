import os
import subprocess
import sys

def process_file(project_dir, file_name, metric_name):
    dir_path = os.path.join('../projects/', project_dir)
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
                    output_file.write(f"{metric_name} {file_name} {metric_val}")
            except ValueError:
                sys.exit()
            except IOError:
                sys.exit()


if __name__ == "__main__":
    # Ensure enough arguments are passed
    if len(sys.argv) != 4:
        print("Usage: python process_file.py <dir_path> <file_name> <metric_name>")
        sys.exit(1)

    # Get the values from the command line arguments
    project_dir = sys.argv[1]
    file_name = sys.argv[2]
    metric_name = sys.argv[3]
    process_file(project_dir, file_name, metric_name)