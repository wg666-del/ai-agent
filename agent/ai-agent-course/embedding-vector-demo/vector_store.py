import os

from dotenv import load_dotenv

from langchain_postgres import PGEngine, PGVectorStore
from sqlalchemy.exc import ProgrammingError

from embedding_factory import create_embeddings

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
VECTOR_TABLE = os.getenv(
    "VECTOR_TABLE",
    "enterprise_knowledge",
)

embeddings = create_embeddings()

pg_engine = PGEngine.from_connection_string(
    url=DATABASE_URL
)


async def initialize_vector_store():
    """
    初始化向量数据库表，并创建 PGVectorStore。
    """

    # 获取实际 Embedding 维度
    sample_vector = embeddings.embed_query(
        "向量维度初始化测试"
    )

    vector_size = len(sample_vector)

    print("Embedding Vector Size:", vector_size)

    # 初始化向量表（幂等：表已存在时直接复用）
    # ainit_vectorstore_table 内部执行的是裸 CREATE TABLE，
    # 没有 IF NOT EXISTS，重复执行会抛 DuplicateTableError。
    try:
        await pg_engine.ainit_vectorstore_table(
            table_name=VECTOR_TABLE,
            vector_size=vector_size,
        )
    except ProgrammingError as exc:
        if "already exists" not in str(getattr(exc, "orig", exc)):
            raise

    # 创建 Vector Store
    vector_store = await PGVectorStore.create(
        engine=pg_engine,
        table_name=VECTOR_TABLE,
        embedding_service=embeddings,
    )

    return vector_store