from langchain_classic.retrievers import ParentDocumentRetriever

from langchain_core.documents import Document
from langchain_core.stores import InMemoryStore

from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

from langchain_text_splitters import RecursiveCharacterTextSplitter


def main():
    embeddings = OllamaEmbeddings(
        model="qwen3-embedding:0.6b"
    )

    vector_store = InMemoryVectorStore(
        embedding=embeddings
    )

    docstore = InMemoryStore()

    parent_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
    )

    child_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=40,
    )

    retriever = ParentDocumentRetriever(
        vectorstore=vector_store,
        docstore=docstore,
        parent_splitter=parent_splitter,
        child_splitter=child_splitter,
    )

    documents = [
        Document(
            page_content=(
                "员工申请年假需要提前三个工作日提交申请。"
                "审批通过后才能休假。"
                "年假天数根据员工工龄及公司制度确定。"
            ),
            metadata={
                "source": "employee-handbook",
                "department": "HR",
            },
        )
    ]

    retriever.add_documents(documents)

    results = retriever.invoke(
        "年假需要提前多久申请？"
    )

    for document in results:
        print(document.page_content)
        print(document.metadata)


if __name__ == "__main__":
    main()