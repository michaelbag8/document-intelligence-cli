# Document Intelligence CLI

A Python command-line tool for extracting and analyzing structured information from text documents.

Document Intelligence CLI reads a text document, identifies values such as email addresses, phone numbers, dates, and IP addresses, validates the extracted candidates, and generates a human-readable report.

The project is built with a simple pipeline architecture that separates document reading, extraction, validation, processing, reporting, and command-line interaction.

## Features

- Extract structured information from text documents
- Validate extracted values
- Generate human-readable reports
- Command-line interface using Python's `argparse`
- Run as a Python module with `python -m docintel`
- Run through the installed `docintel` command
- Handle missing files
- Handle empty documents
- Automated unit and integration tests
- No third-party runtime dependencies

## Supported Extraction Types

The current document-processing pipeline supports:

| Type | Example |
|---|---|
| Email | `support@example.com` |
| Phone number | `+2348012345678` |
| Money | `$2,500.50` |
| Date | `2024-02-29` |
| Hashtag | `#Python` |
| Mention | `@michael` |
| IP address | `192.168.1.1` |

The application uses two stages for most extraction types:

1. **Extraction** identifies candidate values in the document.
2. **Validation** determines whether the candidates satisfy the project's validation rules.

### URL Support

The codebase currently contains URL extraction and URL validation functions.

However, URLs are **not currently connected to the main document-processing pipeline**. Therefore, URLs are not included in the final CLI report.

## Requirements

- Python 3.10 or newer
- Git

The application has no third-party runtime dependencies.

`pytest` is used for development and testing.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/michaelbag8/document-intelligence-cli.git
cd document-intelligence-cli
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

#### Linux, macOS, and WSL

```bash
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the beginning of your terminal prompt.

### 4. Install the project

```bash
python -m pip install -e .
```

The `-e` option installs the project in editable mode. Changes made to the source code are therefore available without reinstalling the package.

### 5. Install the testing dependency

```bash
python -m pip install pytest
```

## Usage

The CLI accepts a document path as a positional argument.

### Run with Python

```bash
python -m docintel sample_data/sample.txt
```

### Run using the installed CLI

```bash
docintel sample_data/sample.txt
```

Both commands execute the same application.

## Command-Line Options

### Display help

```bash
python -m docintel --help
```

or:

```bash
docintel --help
```

### Display the version

```bash
python -m docintel --version
```

or:

```bash
docintel --version
```

## Handling Different Situations

### Existing document

```bash
python -m docintel sample_data/sample.txt
```

The application reads and processes the document and generates a report.

### Missing document

```bash
python -m docintel sample_data/does-not-exist.txt
```

The application reports that the file does not exist and exits with a non-zero status.

### Empty document

```bash
python -m docintel sample_data/empty.txt
```

The application reports:

```text
No content found. Nothing to analyze.
```

An empty document is treated as a valid execution rather than a processing error.

### Missing file path

```bash
python -m docintel
```

`argparse` reports that the required file path argument is missing.

## Sample Input

Example document:

```text
Contact support@acme.com or call +2348012345678.

The transaction amount was $2,500.50 on 2024-02-29.

Follow us on #Python and contact @michael.

The server is available at 192.168.1.1.
```

## Sample Output

```text
Document Intelligence Report
===========================

Emails:
  - support@acme.com

Phone Numbers:
  - +2348012345678

Money:
  - $2,500.50

Dates:
  - 2024-02-29

Hashtags:
  - #Python

Mentions:
  - @michael

Ip Addresses:
  - 192.168.1.1
```

The actual report depends on the contents of the document.

## Architecture

The application follows a simple processing pipeline:

```text
                    ┌──────────────┐
                    │     CLI      │
                    │   cli.py     │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Reader    │
                    │  reader.py   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Processor   │
                    │ processor.py │
                    └──────┬───────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
          ┌──────────────┐    ┌──────────────┐
          │  Extractors  │    │  Validators  │
          │ extractors.py│    │validators.py │
          └──────────────┘    └──────────────┘
                 │                   │
                 └─────────┬─────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Report    │
                    │  report.py   │
                    └──────────────┘
```

### Project Structure

```text
document-intelligence-cli/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── .gitignore
│
├── sample_data/
│   ├── sample.txt
│   └── empty.txt
│
├── src/
│   └── docintel/
│       ├── cli.py
│       ├── extractors.py
│       ├── __main__.py
│       ├── processor.py
│       ├── reader.py
│       ├── report.py
│       └── validators.py
│
└── tests/
    ├── test_cli.py
    ├── test_extractors.py
    ├── test_processor.py
    ├── test_report.py
    └── test_validators.py
```

### Module Responsibilities

#### `cli.py`

Handles command-line arguments and user-facing CLI behavior.

#### `reader.py`

Reads the contents of the supplied document.

#### `extractors.py`

Searches the document for candidate values using regular expressions.

For example, the email extractor searches for strings that look like email addresses.

#### `validators.py`

Validates extracted candidates against the project's validation rules.

The distinction is:

```text
Extractor
    ↓
"Does this text look like a candidate?"

Validator
    ↓
"Does this candidate satisfy our rules?"
```

#### `processor.py`

Coordinates the extractors and validators and produces the structured processing result.

#### `report.py`

Converts the processed data into a human-readable report.

#### `__main__.py`

Allows the application to be executed with:

```bash
python -m docintel
```

## Testing

The project uses `pytest`.

Run the complete test suite with:

```bash
python -m pytest
```

The test suite covers:

* Email extraction and validation
* Phone number extraction and validation
* Money extraction and validation
* Date extraction and validation
* Hashtag extraction
* Mention extraction
* IP address extraction and validation
* Document processing
* Report generation
* Empty documents
* Missing files
* CLI help
* CLI version
* CLI execution

### Run a Specific Test File

```bash
python -m pytest tests/test_extractors.py
```

### Run a Specific Test

```bash
python -m pytest tests/test_validators.py::test_valid_email
```

## Development

### Set Up the Development Environment

```bash
git clone https://github.com/michaelbag8/document-intelligence-cli.git
cd document-intelligence-cli

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -e .
python -m pip install pytest
```

### Run the Application

```bash
python -m docintel sample_data/sample.txt
```

### Run Tests

```bash
python -m pytest
```

### Development Workflow

When changing the project:

```text
Understand the existing behavior
            ↓
Identify the responsible module
            ↓
Make the change
            ↓
Add or update tests
            ↓
Run the test suite
            ↓
Review the result
```

Changes to functionality should be accompanied by appropriate tests.

## Limitations

Document Intelligence CLI currently uses pattern-based extraction and validation. It is not intended to recognize every possible representation of every supported data type.

Current limitations include:

* Extraction relies primarily on regular expressions.
* Supported formats are intentionally limited.
* Phone numbers follow the project's current digit and length rules.
* Money extraction currently focuses on dollar amounts.
* Dates use the `YYYY-MM-DD` format.
* IP addresses are extracted as candidates and then validated as IPv4 addresses.
* Hashtags and mentions follow the project's current regular-expression rules.
* URL extraction and validation exist in the codebase but are not currently part of the main processing pipeline.
* The application currently processes text documents.
* PDF and Microsoft Word documents are not currently supported.
* The application does not determine whether an extracted email address, URL, phone number, or IP address actually exists or is reachable.

## Future Improvements

Possible future improvements include:

* Connect URL extraction to the main processing pipeline
* Support additional date formats
* Improve phone number handling
* Support additional currencies
* Support additional document formats
* Add configurable extraction rules
* Add JSON output
* Improve CLI error handling
* Add code coverage reporting
* Add linting and formatting checks

## Returning to the Project

If the project has already been installed and `.venv` exists, activate the existing environment:

```bash
cd document-intelligence-cli
source .venv/bin/activate
```

Then run:

```bash
python -m docintel sample_data/sample.txt
```

If the virtual environment does not exist, create it first:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## License

This project is licensed under the MIT License.

See the `LICENSE` file for the complete license text.