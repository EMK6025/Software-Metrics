import sys

def metric(file_path):
    # Open the file in read mode
    try:
        with open(file_path, 'r', encoding='utf-8') as java_file:
            for line in java_file:
                count += 1
                #do something
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python \{metrics_name\}.py <dir> <metric_name>")
        sys.exit(1)

    # Get the values from the command line arguments
    file_path = sys.argv[1]

    result = metric(file_path)
    print(result)