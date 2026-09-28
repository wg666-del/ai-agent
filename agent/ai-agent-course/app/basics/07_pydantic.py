# from pydantic import BaseModel

# class ChatRequest(BaseModel):
#     message: str
#     session_id: str | None = None

# request = ChatRequest(message="你好")

# print(request.message)
# print(request.session_id)
# print(request.model_dump())

# from pydantic import BaseModel, ValidationError

# class ChatRequest(BaseModel):
#     message: str
#     session_id: str | None = None

# try:
#     request = ChatRequest(message=123)
# except ValidationError as e:
#     print(e)

from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]
    model: str = "deepseek-chat"

request = ChatRequest(
    messages=[
        Message(role="system", content="你是一个 AI 助手"),
        Message(role="user", content="你好")
    ]
)

print(request.model_dump())