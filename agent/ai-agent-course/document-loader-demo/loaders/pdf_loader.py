from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(file_path)

    loader = PyPDFLoader(
        file_path=str(path),
        mode="page",
    )

    documents = loader.load()

    print(f"PDF 文件：{path.name}")
    print(f"解析页数：{len(documents)}")

    for document in documents:
        print("Page:", document.metadata.get("page"))
        print("Content:", document.page_content[:100])

    return documents


if __name__ == "__main__":
    load_pdf("data/refund_policy.pdf")