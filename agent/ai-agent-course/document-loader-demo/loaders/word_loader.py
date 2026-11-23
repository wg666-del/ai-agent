from pathlib import Path

from langchain_community.document_loaders import Docx2txtLoader


def load_word(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(file_path)

    loader = Docx2txtLoader(
        file_path=str(path)
    )

    documents = loader.load()

    print(f"Word 文件：{path.name}")
    print(f"Document 数量：{len(documents)}")

    for document in documents:
        print(document.page_content[:500])
        print(document.metadata)

    return documents


if __name__ == "__main__":
    load_word("data/contract_template.docx")