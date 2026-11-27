from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b",
)

text = "员工申请年假需要提前三个工作日"

# 单文本向量化
query_vector = embeddings.embed_query(text)

print("向量维度：", len(query_vector))
print("向量前10个值：", query_vector[:10])

# 多文本向量化
texts = [
    "员工申请年假需要提前三个工作日",
    "员工请病假需要提交医院证明",
    "公司服务器部署需要配置Docker",
]

vectors = embeddings.embed_documents(texts)

print("文档数量：", len(vectors))
print("第一个文档向量维度：", len(vectors[0]))