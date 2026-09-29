# from pydantic import BaseModel

# class ChatResponse(BaseModel):
#     answeer: str
#     session_id: str | None = None
#     trace_id: str | None = None

# response = ChatResponse(answeer="你好，我是 AI 助手")

# print(response.model_dump())
# print(response.model_dump(exclude_none=True))

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

user = User(
    id=1,
    name="大伟",
    email="dawei@example.com",
    password="123456"
)

print(user.model_dump(exclude={"password"}))
print(user.model_dump(include={"id", "name"}))