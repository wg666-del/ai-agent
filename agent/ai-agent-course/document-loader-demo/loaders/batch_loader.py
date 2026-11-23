from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
)

from document_cleaner import clean_documents


def load_file(file_path: Path):
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        loader = PyPDFLoader(
            str(file_path),
        )

    elif suffix == ".docx":
        loader = Docx2txtLoader(
            str(file_path)
        )

    elif suffix in [".txt", ".md"]:
        loader = TextLoader(
            str(file_path),
            encoding="utf-8",
        )

    elif suffix == ".csv":
        loader = CSVLoader(
            str(file_path),
            encoding="utf-8",
        )

    else:
        raise  ValueError(
            f"不支持的文件类型：{suffix}"
        )

    documents = loader.load()

    return clean_documents(documents)


def clean_documents(documents):
    return [
        document
        for document in documents
        if document.page_content.strip()
    ]


def load_directory(directory: str):
    root = Path(directory)

    documents = []

    supported_extensions = {
        ".pdf",
        ".docx",
        ".txt",
        ".md",
        ".csv",
    }

    for file_path in root.rglob("*"):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in supported_extensions:
            continue

        try:
            loaded_documents = load_file(
                file_path
            )

            documents.extend(
                loaded_documents
            )

            print(
                f"成功解析：{file_path}"
                f" | Documents: {len(loaded_documents)}"
            )

        except Exception as error:
            print(
                f"解析失败：{file_path}"
                f" | Error: {error}"
            )

    return documents


if __name__ == "__main__":
    documents = load_directory(
        "data"
    )

    print(
        f"总共解析 {len(documents)} 条 Documents"
    )