import argparse

from .reader import read_document

YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"


def main():
    parser = argparse.ArgumentParser(
        description="Document Intelligence CLI - Extract information from text documents."
    )
    parser.add_argument("file_path", help="Path to the document file")
    args = parser.parse_args()

    try:
        content = read_document(args.file_path)
        if not content:
            print(f"{YELLOW}No content found. Nothing to analyze.{RESET}")
        else:
            print(content)

    except FileNotFoundError:
        print(f"{RED}File does not exist{RESET}")


if __name__ == "__main__":
    main()