from langchain_community.document_loaders import JSONLoader


def load_json(file_path: str):
    loader = JSONLoader(
        file_path=file_path,
        jq_schema=".policies[]",
        content_key="content",
        metadata_func=lambda record, metadata: {
            **metadata,
            "title": record.get("title"),
            "document_type": "json",
        },
    )

    documents = loader.load()

    for document in documents:
        print(document.page_content)
        print(document.metadata)

    return documents


if __name__ == "__main__":
    load_json("data/employee-handbook.json")