import io
import os
import shutil
from pathlib import Path

import pymupdf
import pytesseract

from PIL import Image

from langchain_core.documents import Document


def _configure_tesseract() -> None:
    """在 Windows 上未加入 PATH 时，自动定位 Tesseract 可执行文件。"""
    if shutil.which("tesseract"):
        return

    candidates = [
        Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
        / "Tesseract-OCR"
        / "tesseract.exe",
        Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"))
        / "Tesseract-OCR"
        / "tesseract.exe",
        Path(os.environ.get("LOCALAPPDATA", ""))
        / "Programs"
        / "Tesseract-OCR"
        / "tesseract.exe",
    ]

    for candidate in candidates:
        if candidate.is_file():
            pytesseract.pytesseract.tesseract_cmd = str(candidate)
            return


def load_scanned_pdf(file_path: str) -> list[Document]:
    path = Path(file_path)

    _configure_tesseract()

    documents: list[Document] = []

    with pymupdf.open(path) as pdf:
        for page_index, page in enumerate(pdf):
            pixmap = page.get_pixmap(
                dpi=200,
            )

            # 直接在内存中转换，避免写临时文件（原 /tmp 路径在 Windows 上不存在）
            image = Image.open(
                io.BytesIO(pixmap.tobytes("png"))
            )

            text = pytesseract.image_to_string(
                image,
                lang="chi_sim+eng",
            )

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": path.name,
                        "page": page_index,
                        "document_type": "scanned_pdf",
                    }
                )
            )

    return documents


if __name__ == "__main__":
    documents = load_scanned_pdf(
        "data/refund_policy.pdf"
    )

    for document in documents:
        print(document.page_content)