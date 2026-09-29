# from pydantic import BaseModel, Field

# class ChatRequest(BaseModel):
#     message: str = Field(..., description="用户输入的问题"),
#     model: str = Field(default="deepseek-chat", description="模型名称")
#     temperature: float = Field(default=0.7, description="模型温度")
#     stream: bool = Field(default=True, description="是否流式输出")

# request = ChatRequest(message="什么是 AI Agent？")

# print(request.model_dump())

# from pydantic import BaseModel, Field, ValidationError

# class ChatRequest(BaseModel):
#     message: str = Field(
#         ...,
#         min_length=1,
#         max_length=2000,
#         description="用户输入的问题"
#     )

# try:
#     request = ChatRequest(message="")
# except ValidationError as e:
#     print(e)

# from pydantic import BaseModel, Field, ValidationError

# class ChatRequest(BaseModel):
#     message: str
#     temperature: float = Field(
#         default=0.7,
#         ge=0,
#         le=2,
#         description="模型温度，范围 0 到 2"
#     )

# try:
#     request = ChatRequest(
#         message="你好",
#         temperature=3
#     )
# except ValidationError as e:
#     print(e)

from pydantic import BaseModel, Field

class ChatSession(BaseModel):
    session_id: str
    messages: list[str] = Field(default_factory=list)

session1 = ChatSession(session_id="s1")
session2 = ChatSession(session_id="s2")

session1.messages.append("你好")

print(session1.model_dump())
print(session2.model_dump())