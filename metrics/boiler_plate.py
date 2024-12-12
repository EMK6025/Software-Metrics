import sys

def metric(file_path):
    count = 0
    # Open the file in read mode
    try:
        with open(file_path, 'r', encoding='utf-8') as java_file:
            for line in java_file:
                count += 1
                #do something
        return count
    # Handle exceptions
    except FileNotFoundError:
        return "MetricFileNotFoundError"
    except IOError as e:
        return "MetricIOError"

if __name__ == "__main__":
    # Ensure enough arguments are passed
    if len(sys.argv) != 2:
        print("Usage: python <metrics_name>.py <file_path>")
        sys.exit(1)

    # Get the values from the command line arguments
    file_path = sys.argv[1]

    # Print the result of metric
    print(metric(file_path)) 