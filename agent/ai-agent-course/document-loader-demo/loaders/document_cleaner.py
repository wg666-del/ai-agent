import re

from langchain_core.documents import Document


def clean_document(
    document: Document,
) -> Document:
    text = document.page_content

    # 去除空白行
    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    # 去除连续空格
    text = re.sub(
        r"[ \t]{2,}",
        " ",
        text,
    )

    # 去除首尾空白
    text = text.strip()

    # 过滤无效内容
    if not text:
        return Document(
            page_content="",
            metadata=document.metadata,
        )

    return Document(
        page_content=text,
        metadata=document.metadata,
    )


def clean_documents(
    documents: list[Document],
) -> list[Document]:
    cleaned = []

    for document in documents:
        result = clean_document(document)

        if result.page_content:
            cleaned.append(result)

    return cleaned