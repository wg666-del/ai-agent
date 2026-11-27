import os

from dotenv import load_dotenv
from langchain_core.embeddings import Embeddings
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def create_embeddings() -> Embeddings:
    provider = os.getenv(
        "EMBEDDING_PROVIDER",
        "ollama"
    )

    if provider == "ollama":
        return OllamaEmbeddings(
            model=os.getenv(
                "OLLAMA_EMBEDDING_MODEL",
                "qwen3-embedding:0.6b",
            ),
            base_url=os.getenv(
                "OLLAMA_BASE_URL",
                "http://localhost:11434"
            ),
        )

    if provider == "openai":
        return OpenAIEmbeddings(
            model=os.getenv(
                "OPENAI_EMBEDDING_MODEL",
                "text-embedding-3-small"
            ),
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    raise ValueError(
        f"不支持的 Embedding Provider: {provider}"
    )