import sys
from .reader import read_document

def main():
    try:
        file_path = sys.argv[1]
        content = read_document(file_path)
        if not content:
            print("File is empty")
        else:
            print(content)
    except FileNotFoundError:
        print("File does not exist")
    except IndexError:
        print("Please provide a file path as an argument")
