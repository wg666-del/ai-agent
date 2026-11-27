from langchain_core.documents import Document
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="enterprise_knowledge",
    embedding_function=embeddings,
    persist_directory="./data/chroma_db",
)

docs = [
    Document(
        page_content="订单未发货时，可以申请取消订单并退款。",
        metadata={
            "tenant_id": "tenant_001",
            "doc_type": "after_sales",
        },
    )
]

vector_store.add_documents(
    documents=docs,
    ids=["chunk_001"],
)

results = vector_store.similarity_search(
    query="没发货可以退款吗？",
    k=3,
    filter={
        "tenant_id": "tenant_001",
        "doc_type": "after_sales",
    },
)