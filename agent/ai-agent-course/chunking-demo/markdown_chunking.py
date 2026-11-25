from pathlib import Path

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)


def main():
    text = Path(
        "data/employee-handbook.md"
    ).read_text(encoding="utf-8")

    # 第一步：按照 Markdown 标题切分
    headers_to_split_on = [
        ("#", "Header1"),
        ("##", "Header2"),
        ("###", "Header3"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False,
    )

    header_documents = markdown_splitter.split_text(text)

    print("标题切分数量:", len(header_documents))

    # 第二步：对过长的章节进一步切分
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80,
    )

    chunks = recursive_splitter.split_documents(
        header_documents
    )

    for index, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {index}")
        print("Content:", chunk.page_content)
        print("Metadata:", chunk.metadata)


if __name__ == "__main__":
    main()