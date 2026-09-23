import argparse
import sys
from importlib.metadata import version

from .processor import process_document
from .reader import read_document
from .report import generate_report


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Document Intelligence CLI - Extract information from text documents."
    )

    parser.add_argument(
        "file_path",
        help="Path to the document file"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"Document Intelligence CLI version {version('document-intelligence-cli')}",
        help="Show the version of the Document Intelligence CLI",
    )

    args = parser.parse_args()

    try:
        content = read_document(args.file_path)

        if not content:
            print(f"No content found. Nothing to analyze.")
        else:
            data = process_document(content)
            report = generate_report(data)
            print(report)

    except FileNotFoundError:
        print(f"File does not exist")
        sys.exit(1)

    except PermissionError:
        print(f"Permission denied: cannot read file")
        sys.exit(1)