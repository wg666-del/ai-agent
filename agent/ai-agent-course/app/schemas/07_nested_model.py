# from pydantic import BaseModel, Field

# class Message(BaseModel):
#     role: str = Field(..., description="消息角色")
#     content: str = Field(..., min_length=1, description="消息内容")

# class ChatRequest(BaseModel):
#     messages: list[Message] = Field(..., description="对话消息列表")
#     model: str = Field(default="deepseek-chat", description="模型名称")

# request = ChatRequest(
#     messages=[
#         Message(role="system", content="你是一个专业的 AI 助手"),
#         Message(role="user", content="什么是 RAG？")
#     ]
# )

# print(request.model_dump())


from pydantic import BaseModel, Field, ValidationError

class Message(BaseModel):
    role: str = Field(..., description="消息角色")
    content: str = Field(..., min_length=1, description="消息内容")

class ChatRequest(BaseModel):
    messages: list[Message]

try:
    request = ChatRequest(
        messages=[
            { "role": "user", "content": "" }
        ]
    )
except ValidationError as e:
    print(e)