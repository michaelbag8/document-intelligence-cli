import argparse
from .reader import read_document

def main():
    parser = argparse.ArgumentParser(description="Document Intelligence CLI - Extract information from text documents.")
    parser.add_argument("file_path", help="Path to the document file")
    args = parser.parse_args()

    try:
        content = read_document(args.file_path)
        if not content:
            print("\033[33mFile is empty\033[0m")

        else:
            print(content)
        
    except FileNotFoundError:
        print("\033[31mFile does not exist\033[0m")
