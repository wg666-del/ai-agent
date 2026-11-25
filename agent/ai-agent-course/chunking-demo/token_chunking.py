from langchain_text_splitters import TokenTextSplitter


def main():
    text = """
    RAG 是 Retrieval Augmented Generation 的缩写。
    它通过检索外部知识，为大语言模型提供额外上下文。
    企业知识库通常使用 RAG 实现文档问答、制度查询和知识助手。
    """

    splitters = TokenTextSplitter(
        encoding_name="cl100k_base",
        chunk_size=100,
        chunk_overlap=20,
    )

    chunks = splitters.split_text(text)

    for index, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {index}")
        print(chunk)


if __name__ == "__main__":
    main()