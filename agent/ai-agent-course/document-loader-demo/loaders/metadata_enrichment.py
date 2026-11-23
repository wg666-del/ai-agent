from pathlib import Path

from langchain_core.documents import Document


def enrich_metadata(
    documents: list[Document],
    file_path: str,
    tenant_id: str,
    department: str,
    category: str,
):
    path = Path(file_path)

    enriched = []

    for document in documents:
        metadata = {
            **document.metadata,
            "source": path.name,
            "document_id": path.stem,
            "tenant_id": tenant_id,
            "department": department,
            "category": category,
            "file_type": path.suffix.lower(),
        }

        enriched.append(
            Document(
                page_content=document.page_content,
                metadata=metadata,
            )
        )

    return enriched