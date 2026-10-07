from app.schemas.chat import ChatMessage, ChatRequest, MessageRole


request = ChatRequest(
    messages=[
        ChatMessage(
            role=MessageRole.SYSTEM,
            content="你是一个专业 AI 助手"
        ),
        ChatMessage(
            role=MessageRole.USER,
            content="什么是 AI Agent？"
        )
    ],
    model="deepseek-chat",
    temperature=0.7,
    stream=False,
)

print(request.model_dump())