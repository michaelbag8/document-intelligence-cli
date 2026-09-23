import pytest

from docintel.reader import read_document


def test_read_document(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Hello, Document Intelligence!")

    result = read_document(file)

    assert result == "Hello, Document Intelligence!"


def test_read_empty_document(tmp_path):
    file = tmp_path / "empty.txt"
    file.write_text("")

    result = read_document(file)

    assert result == ""


def test_read_document_with_unicode(tmp_path):
    file = tmp_path / "unicode.txt"
    file.write_text("Café, Nigeria 🇳🇬, Python")

    result = read_document(file)

    assert result == "Café, Nigeria 🇳🇬, Python"


def test_read_document_file_not_found(tmp_path):
    file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        read_document(file)


def test_read_document_directory(tmp_path):
    with pytest.raises(IsADirectoryError):
        read_document(tmp_path)