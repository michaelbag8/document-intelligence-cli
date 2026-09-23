import subprocess
import pytest

def test_cli_valid_document():
    result = subprocess.run(
        ["python", "-m", "docintel", "sample_data/sample.txt"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0


def test_cli_invalid_document():
    result = subprocess.run(
        ["python", "-m", "docintel", "sample_data/invalid_sample.txt"],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0

def test_cli_help():
    result = subprocess.run(
        ["python", "-m", "docintel", "--help"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "usage" in result.stdout.lower()

def test_cli_version():
    result = subprocess.run(
        ["python", "-m", "docintel", "--version"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "version" in result.stdout.lower()  

def test_cli_report_generation():
    result = subprocess.run(
        ["python", "-m", "docintel", "sample_data/sample.txt"],
        capture_output=True,
        text=True
    ) 

    assert "Document Intelligence Report" in result.stdout



def test_cli_report_contains_email_and_phone():
    result = subprocess.run(
        ["python", "-m", "docintel", "sample_data/sample.txt"],
        capture_output=True,
        text=True
    )
    assert "support@acme.com" in result.stdout
    assert "+2348012345678" in result.stdout


def test_cli_empty_file():
    result = subprocess.run(
        ["python", "-m", "docintel", "sample_data/empty.txt"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "No content found. Nothing to analyze." in result.stdout


def test_cli_missing_file():
    result = subprocess.run(
        ["python", "-m", "docintel", "sample_data/non_existent.txt"],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0
    assert "File does not exist" in result.stdout   

def test_cli_invalid_file_format():
    result = subprocess.run(
        ["python", "-m", "docintel", "sample_data/sample.pdf"],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0
    assert "File does not exist" in result.stdout

def test_cli_permission_error(monkeypatch):
    def mock_read_document(file_path):
        raise PermissionError

    monkeypatch.setattr("docintel.cli.read_document", mock_read_document)

    from docintel.cli import main

    monkeypatch.setattr(
        "sys.argv",
        ["docintel", "sample_data/sample.txt"],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1