def read_document(file_path: str) -> str:

    with open(file_path, encoding="utf-8") as file:

        return file.read()
