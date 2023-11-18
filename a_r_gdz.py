import argparse
def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"Number of words in {file_path}: {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if  __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File reader and word counter")
    parser.add_argument("--file", help="Path to the file to read", required=True)
    args = parser.parse_args()
    process_file(args.file)