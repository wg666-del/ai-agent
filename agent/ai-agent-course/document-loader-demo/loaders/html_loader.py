from pathlib import Path

from bs4 import BeautifulSoup

from langchain_core.documents import Document


def load_html(file_path: str):
    path = Path(file_path)

    html = path.read_text(
        encoding="utf-8"
    )

    soup = BeautifulSoup(
        html,
        "lxml",
    )

    # 移除无关内容
    for tag in soup.select(
        "script, style, nav, footer, header"
    ):
        tag.decompose()

    title = (
        soup.title.get_text(strip=True)
        if soup.title
        else path.stem
    )

    content = soup.get_text(
        separator="\n",
        strip=True,
    )

    document = Document(
        page_content=content,
        metadata={
            "source": path.name,
            "title": title,
            "document_type": "html",
        }
    )

    return [document]


if __name__ == "__main__":
    documents = load_html(
        "data/employee-handbook.html"
    )

    for document in documents:
        print(document.page_content)
        print(document.metadata)