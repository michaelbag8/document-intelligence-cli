import argparse
import sys
from importlib.metadata import version

from .processor import process_document
from .reader import read_document
from .report import generate_report


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="docintel",
        description=(
            "Document Intelligence CLI - Extract information from text documents."
        ),
    )

    parser.add_argument(
        "file_path",
        help="Path to the document file",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=(
            f"Document Intelligence CLI version {version('document-intelligence-cli')}"
        ),
        help="Show the version of the Document Intelligence CLI",
    )

    args = parser.parse_args()

    try:
        content = read_document(args.file_path)

        if not content:
            print("No content found. Nothing to analyze.")
        else:
            data = process_document(content)
            report = generate_report(data)
            print(report)

    except FileNotFoundError:
        print(
            f"File does not exist: {args.file_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    except PermissionError:
        print(
            f"Permission denied: cannot read file: {args.file_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    except IsADirectoryError:
        print(
            f"Expected a file, but received a directory: {args.file_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    except UnicodeDecodeError:
        print(
            f"File is not valid UTF-8 text: {args.file_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    except OSError as error:
        print(
            f"Unable to read file '{args.file_path}': {error}",
            file=sys.stderr,
        )
        sys.exit(1)
