# Document Intelligence CLI

A Python command-line tool for extracting and analyzing information from text documents.

## Requirements

* Python 3.10 or newer
* Git

## 1. Clone the repository

```bash
git clone <repository-url>
cd document-intelligence-cli
```

Replace `<repository-url>` with the URL of this repository.

## 2. Create a virtual environment

Create a virtual environment inside the project:

```bash
python3 -m venv .venv
```

## 3. Activate the virtual environment

On Linux/macOS/WSL:

```bash
source .venv/bin/activate
```

You should see `(.venv)` at the beginning of your terminal prompt.

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 4. Install the project

Install the project in editable mode:

```bash
python -m pip install -e .
```

The `-e` option means that changes made to the source code are immediately available without reinstalling the project.

## 5. Run the program

Run the CLI with a text file:

```bash
python -m docintel sample_data/sample.txt
```

You can also use the installed CLI command if the project defines the `docintel` entry point:

```bash
docintel sample_data/sample.txt
```

## 6. Test different situations

### Read an existing document

```bash
python -m docintel sample_data/sample.txt
```

### Try a file that does not exist

```bash
python -m docintel sample_data/does-not-exist.txt
```

The program should handle the error gracefully.

### Run without a file

```bash
python -m docintel
```

The program should tell you that a file path is required.

### Test an empty file

Create an empty file:

```bash
touch sample_data/empty.txt
```

Then run:

```bash
python -m docintel sample_data/empty.txt
```

The program should report that the file is empty.

## 7. Deactivate the virtual environment

When you are finished:

```bash
deactivate
```

## Starting the project again later

After cloning the repository, or when returning to the project after a fresh setup:

```bash
cd document-intelligence-cli
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m docintel sample_data/sample.txt
```

If the `.venv` directory already exists, do **not** create it again. Just activate it:

```bash
source .venv/bin/activate
```

Then run:

```bash
python -m docintel sample_data/sample.txt
```

## Development

Run the test suite with:

```bash
python -m pytest
```

As the project grows, additional CLI options and commands will be documented here.
