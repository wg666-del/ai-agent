import re
from abc import ABC, abstractmethod

from app.document_chunking.schemas import (
    ChunkConfig,
    ChunkDocument,
    ChunkResult,
    ChunkStrategy,
)
from app.document_parsing.schemas import (
    ParsedDocument,
    ParsedElement,
    ParsedElementType,
)


class BaseChunker(ABC):
    def __init__(
        self,
        config: ChunkConfig,
    ):
        if config.chunk_size <= 0:
            raise ValueError("chunk_size 必须大于 0")

        if config.chunk_overlap < 0:
            raise ValueError("chunk_overlap 不能小于 0")

        if config.chunk_overlap >= config.chunk_size:
            raise ValueError("chunk_overlap 必须小于 chunk_size")

        self.config = config

    @abstractmethod
    def split(
        self,
        document: ParsedDocument,
    ) -> ChunkResult:
        raise NotImplementedError

    def build_chunk_id(
        self,
        document_id: str,
        chunk_index: int,
    ) -> str:
        return f"{document_id}_chunk_{chunk_index}"

    def build_base_metadata(
        self,
        document: ParsedDocument,
        chunk_index: int,
    ) -> dict:
        metadata = {
            **document.metadata,
            "document_id": document.document_id,
            "document_title": document.title,
            "file_name": document.file_name,
            "file_type": document.file_type,
            "source_path": document.source_path,
            "chunk_index": chunk_index,
        }

        return metadata

    def create_chunk(
        self,
        document: ParsedDocument,
        content: str,
        chunk_index: int,
        strategy: ChunkStrategy,
        extra_metadata: dict | None = None,
    ) -> ChunkDocument:
        metadata = self.build_base_metadata(
            document=document,
            chunk_index=chunk_index,
        )

        if extra_metadata:
            metadata.update(extra_metadata)

        return ChunkDocument(
            chunk_id=self.build_chunk_id(
                document.document_id,
                chunk_index,
            ),
            document_id=document.document_id,
            title=document.title,
            content=content.strip(),
            chunk_index=chunk_index,
            strategy=strategy,
            metadata=metadata,
        )

    def should_keep_chunk(
        self,
        content: str,
    ) -> bool:
        return len(content.strip()) >= self.config.min_chunk_size


class FixedSizeChunker(BaseChunker):
    def split(
        self,
        document: ParsedDocument,
    ) -> ChunkResult:
        text = document.text
        chunks: list[ChunkDocument] = []

        start = 0
        chunk_index = 0

        while start < len(text):
            end = start + self.config.chunk_size
            content = text[start:end]

            if self.should_keep_chunk(content):
                chunks.append(
                    self.create_chunk(
                        document=document,
                        content=content,
                        chunk_index=chunk_index,
                        strategy=ChunkStrategy.FIXED_SIZE,
                        extra_metadata={
                            "start_char": start,
                            "end_char": min(end, len(text)),
                        },
                    )
                )
                chunk_index += 1

            if end >= len(text):
                break

            start = end - self.config.chunk_overlap

        return ChunkResult(
            document_id=document.document_id,
            title=document.title,
            total_chunks=len(chunks),
            strategy=ChunkStrategy.FIXED_SIZE,
            chunks=chunks,
            warnings=[
                "FixedSizeChunker 只适合教学或兜底，不建议作为企业默认策略。"
            ]
        )


class ParagraphChunker(BaseChunker):
    def split(
        self,
        document: ParsedDocument,
    ) -> ChunkResult:
        paragraphs = [
            paragraph.strip()
            for paragraph in re.split(r"\n\s*\n", document.text)
            if paragraph.strip()
        ]

        chunks: list[ChunkDocument] = []
        current_parts: list[str] = []
        current_size = 0
        chunk_index = 0

        for paragraph in paragraphs:
            paragraph_size = len(paragraph)

            if current_parts and current_size + paragraph_size > self.config.chunk_size:
                content = "\n\n".join(current_parts)

                if self.should_keep_chunk(content):
                    chunks.append(
                        self.create_chunk(
                            document=document,
                            content=content,
                            chunk_index=chunk_index,
                            strategy=ChunkStrategy.PARAGRAPH,
                            extra_metadata={
                                "paragraph_count": len(current_parts),
                            },
                        )
                    )
                    chunk_index += 1

                # 简单 overlap：保留最后一个段落作为上下文。
                if self.config.chunk_overlap > 0 and current_parts:
                    current_parts = [current_parts[-1]]
                    current_size = len(current_parts[-1])
                else:
                    current_parts = []
                    current_size = 0

            current_parts.append(paragraph)
            current_size += paragraph_size

        if current_parts:
            content = "\n\n".join(current_parts)

            if self.should_keep_chunk(content):
                chunks.append(
                    self.create_chunk(
                        document=document,
                        content=content,
                        chunk_index=chunk_index,
                        strategy=ChunkStrategy.PARAGRAPH,
                        extra_metadata={
                            "paragraph_count": len(current_parts),
                        },
                    )
                )

        return ChunkResult(
            document_id=document.document_id,
            title=document.title,
            total_chunks=len(chunks),
            strategy=ChunkStrategy.PARAGRAPH,
            chunks=chunks,
        )



class PageChunker(BaseChunker):
    def split(
        self,
        document: ParsedDocument,
    ) -> ChunkResult:
        chunks: list[ChunkDocument] = []
        chunk_index = 0

        page_elements = [
            element for element in document.elements
            if element.page_number is not None
        ]

        if not page_elements:
            return ChunkResult(
                document_id=document.document_id,
                title=document.title,
                total_chunks=0,
                strategy=ChunkStrategy.PAGE,
                chunks=[],
                warnings=["当前文档没有 page_number，无法按页切分。"],
            )

        for element in page_elements:
            content = element.content

            if not self.should_keep_chunk(content):
                continue

            chunks.append(
                self.create_chunk(
                    document=document,
                    content=content,
                    chunk_index=chunk_index,
                    strategy=ChunkStrategy.PAGE,
                    extra_metadata={
                        "page_number": element.page_number,
                        "element_id": element.element_id,
                        "element_type": element.type.value,
                    },
                )
            )

            chunk_index += 1

        return ChunkResult(
            document_id=document.document_id,
            title=document.title,
            total_chunks=len(chunks),
            strategy=ChunkStrategy.PAGE,
            chunks=chunks,
        )


class ElementChunker(BaseChunker):
    def split(
        self,
        document: ParsedDocument,
    ) -> ChunkResult:
        chunks: list[ChunkDocument] = []
        chunk_index = 0

        for element in document.elements:
            content = element.content

            if not self.should_keep_chunk(content):
                continue

            chunks.append(
                self.create_chunk(
                    document=document,
                    content=content,
                    chunk_index=chunk_index,
                    strategy=ChunkStrategy.ELEMENT,
                    extra_metadata={
                        "element_id": element.element_id,
                        "element_type": element.type.value,
                        "page_number": element.page_number,
                        "order_index": element.order_index,
                    },
                )
            )

            chunk_index += 1

        return ChunkResult(
            document_id=document.document_id,
            title=document.title,
            total_chunks=len(chunks),
            strategy=ChunkStrategy.ELEMENT,
            chunks=chunks,
        )