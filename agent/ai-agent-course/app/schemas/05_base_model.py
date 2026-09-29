# from pydantic import BaseModel

# class ChatRequest(BaseModel):
#     message: str
#     model: str = "deepseek-chat"
#     temperature: float = 0.7
#     stream: bool = True

# request = ChatRequest(
#     message="什么是 AI Agent？"
# )

# print(request)
# print(request.message)
# print(request.model)
# print(request.temperature)
# print(request.stream)

# from pydantic import BaseModel, ValidationError

# class ChatRequest(BaseModel):
#     message: str
#     model: str = "deepseek-chat"
#     temperature: float = 0.7
#     stream: bool = True

# try:
#     request = ChatRequest(
#         message=123,
#         temperature="abc"
#     )
# except ValidationError as e:
#     print(e)

# from pydantic import BaseModel

# class ChatRequest(BaseModel):
#     message: str
#     model: str = "deepseek-chat"
#     temperature: float = 0.7
#     stream: bool = True

# request = ChatRequest(
#     message="什么是 RAG？"
# )

# data = request.model_dump()

# print(data)
# print(type(data))

from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    model: str = "deepseek-chat"
    temperature: float = 0.7
    stream: bool = True

request = ChatRequest(
    message="什么是 LangGraph？"
)

json_str = request.model_dump_json()

print(json_str)
print(type(json_str))