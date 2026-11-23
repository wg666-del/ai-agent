from pathlib import Path

from langchain_community.document_loaders import TextLoader


def load_markdown(file_path: str):
    path = Path(file_path)

    loader = TextLoader(
        file_path=str(path),
        encoding="utf-8",
    )

    documents = loader.load()

    for document in documents:
        print(document.page_content)
        print(document.metadata)

    return documents


if __name__ == "__main__":
    load_markdown(
        "data/employee_handbook.md"
    )