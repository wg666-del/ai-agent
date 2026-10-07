import asyncio
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="用户输入的消息")

class ChatResponse(BaseModel):
    answer: str = Field(..., description="AI agent的回复")

async def call_llm(message: str) -> str:
    await asyncio.sleep(1)
    return f"AI 回答：你问的是 {message}"

async def chat_service(request: ChatRequest) -> ChatResponse:
    answer = await call_llm(request.message)
    return ChatResponse(answer=answer)

async def main():
    request = ChatRequest(message="什么是 LangGraph？")
    response = await chat_service(request)
    print(response.model_dump())


asyncio.run(main())