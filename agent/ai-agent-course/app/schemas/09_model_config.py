# from pydantic import BaseModel, Field

# class ChatRequest(BaseModel):
#     session_id: str = Field(alias="sessionId")
#     message: str

# request = ChatRequest(
#     sessionId="s_10001",
#     message="你好"
# )

# print(request.session_id)
# print(request.model_dump())
# print(request.model_dump(by_alias=True))

# from pydantic import BaseModel, ConfigDict, Field

# class ChatRequest(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)

#     session_id: str = Field(alias="sessionId")
#     message: str

# request1 = ChatRequest(
#     sessionId="s_10001",
#     message="你好"
# )

# request2 = ChatRequest(
#     session_id="s_10002",
#     message="你好"
# )

# print(request1.model_dump())
# print(request2.model_dump())

from pydantic import BaseModel, ConfigDict, ValidationError

class ChatRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    message: str
    model: str = "deepseek-chat"

try:
    request = ChatRequest(
        message="你好",
        model="deepseek-chat",
        unknown_field="xx"
    )
except ValidationError as e:
    print(e)