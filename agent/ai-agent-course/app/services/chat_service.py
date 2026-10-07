import asyncio
import uuid

from app.schemas.chat import (
  ChatRequest,
  ChatResponse,
  MessageRole,
  SourceDocument,
  TokenUsage,
)

async def chat_with_ai(request: ChatRequest) -> ChatResponse:
    await asyncio.sleep(1)  # 模拟延迟

    latest_user_message = get_latest_user_message(request)

    if "AI Agent" in latest_user_message:
        answer = "AI Agent是能够理解目标、规划步骤并调用工具完成任务的智能体。"
    elif "RAG" in latest_user_message:
        answer = "RAG（Retrieval-Augmented Generation）是一种结合检索和生成的技术，用于增强语言模型的回答能力。"
    elif "LangGraph" in latest_user_message:
        answer = "LangGraph是一个用于构建和管理语言模型图的工具。"
    else:
        answer = f"这是一个模拟回答：你刚才问的是「{latest_user_message}」。"

    usage = TokenUsage(
        prompt_tokens=count_mock_tokens_from_messages(request),
        completion_tokens=len(answer),  # 简单模拟
        total_tokens=count_mock_tokens_from_messages(request) + len(answer),
    )

    sources = build_mock_sources(latest_user_message)

    return ChatResponse(
        answer=answer,
        model=request.model,
        session_id=request.session_id or f"s_{uuid.uuid4().hex[:8]}",
        message_id=f"m_{uuid.uuid4().hex[:8]}",
        usage=usage,
        sources=sources,
        trace_id=f"t_{uuid.uuid4().hex[:8]}",
    )

def get_latest_user_message(request: ChatRequest) -> str:
    for message in reversed(request.messages):
        if message.role == MessageRole.USER:
            return message.content
    return request.messages[-1].content

def count_mock_tokens_from_messages(request: ChatRequest) -> int:
    # 简单模拟 token 计数，每个字符算作一个 token
    return sum(len(message.content) for message in request.messages)

def build_mock_sources(question: str) -> list[SourceDocument]:
    if "RAG" not in question and "知识库" not in question:
        return []

    return [
        SourceDocument(
            document_id="doc_001",
            title="企业知识库说明文档",
            content="RAG 是 Retrieval Augmented Generation，用于结合外部知识增强大模型回答。",
            score=0.89,
            metadata={
                "source": "mock",
                "page": 1,
            },
        )
    ]