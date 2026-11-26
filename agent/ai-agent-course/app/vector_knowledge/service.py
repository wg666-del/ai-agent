from app.document_chunking.schemas import (
    ChunkConfig,
    ChunkDocument,
    ChunkStrategy,
)
from app.document_chunking.service import document_chunking_service
from app.document_parsing.service import document_parsing_service
from app.vector_knowledge.embedding import EmbeddingModelFactory
from app.vector_knowledge.schemas import (
    EmbeddedChunk,
    EmbeddingConfig,
    IndexBuildResult,
    VectorSearchRequest,
    VectorSearchResponse,
    VectorStoreProvider,
)
from app.vector_knowledge.vector_store import InMemoryVectorStore


class EmbeddingService:
    def __init__(
        self,
        config: EmbeddingConfig | None = None,
    ):
        self.config = config or EmbeddingConfig()
        self.model = EmbeddingModelFactory().create(self.config)

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        return self.model.embed_text(text)

    def embed_chunks(
        self,
        chunks: list[ChunkDocument],
    ) -> list[EmbeddedChunk]:
        texts = [
            chunk.content
            for chunk in chunks
        ]

        embeddings = self.model.embed_texts(texts)

        embedded_chunks: list[EmbeddedChunk] = []

        for chunk, embedding in zip(chunks, embeddings):
            embedded_chunks.append(
                EmbeddedChunk(
                    chunk_id=chunk.chunk_id,
                    document_id=chunk.document_id,
                    content=chunk.content,
                    embedding=embedding,
                    metadata={
                        **chunk.metadata,
                        "embedding_provider": self.config.provider.value,
                        "embedding_model": self.config.model_name,
                        "embedding_dimension": self.config.dimension,
                    }
                )
            )

        return embedded_chunks