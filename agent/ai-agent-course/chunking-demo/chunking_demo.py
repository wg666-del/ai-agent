from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def main():
    file_path = Path("data/employee-handbook.txt")

    text = file_path.read_text(encoding="utf-8")

    document = Document(
        page_content=text,
        metadata={
            "source": str(file_path),
            "document_id": "employee-handbook",
            "department": "HR",
        },
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=30,
        length_function=len,
        separators=[
            "\n\n",
            "\n",
            "。",
            "！",
            "？",
            "；",
            "，",
            " ",
            "",
        ],
    )

    chunks = splitter.split_documents([document])

    print(f"原文长度：{len(text)}")
    print(f"Chunk 数量：{len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n===== Chunk {index} =====")
        print("Content:", chunk.page_content)
        print("Metadata:", chunk.metadata)


if __name__ == "__main__":
    main()