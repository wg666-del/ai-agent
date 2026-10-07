import asyncio
from fastapi import HttpException
from app.schemas.chat import ChatRequest, ChatResponse

async def chat_with_ai(request: ChatRequest) -> ChatResponse:
    await asyncio.sleep(1)  # 模拟延迟
    supported_models = ["deepseek-chat", "qwen-plus", "gpt-4o-mini"]

    if request.model not in supported_models:
        raise HttpException(
            status_code=400,
            detail=f"不支持的模型：{request.model}"
        )

    if "AI Agent" in request.message:
        answer = "AI Agent是能够理解目标、规划步骤并调用工具完成任务的智能体。"
    elif "RAG" in request.message:
        answer = "RAG（Retrieval-Augmented Generation）是一种结合检索和生成的技术，用于增强语言模型的回答能力。"
    else:
        answer = f"这是一个模拟回答：你刚才问的是「{request.message}」。"

    return ChatResponse(answer=answer, model=request.model)