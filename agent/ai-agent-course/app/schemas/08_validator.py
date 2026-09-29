# from pydantic import BaseModel, Field, ValidationError, field_validator

# class ChatRequest(BaseModel):
#     message: str = Field(..., min_length=1)

#     @field_validator("message")
#     @classmethod
#     def validate_message(cls, value: str) -> str:
#         if "广告" in value:
#             raise ValueError("message 不能包含广告内容")

#         return value

# try:
#     request = ChatRequest(message="这是一条广告")
# except ValidationError as e:
#     print(e)

# from pydantic import BaseModel, field_validator

# class UserCreateRequest(BaseModel):
#     email: str

#     @field_validator("email")
#     @classmethod
#     def mormalize_email(cls, value: str) -> str:
#         return value.strip().lower()

# request = UserCreateRequest(email=" DAWEI@EXAMPLE.COM ")

# print(request.email)

from pydantic import BaseModel, Field, ValidationError, model_validator

class ChatRequest(BaseModel):
    message: str
    stream: bool = True
    callback_url: str | None = None

    @model_validator(mode="after")
    def validate_callback_url(self):
        if self.stream is False and self.callback_url is None:
            raise ValueError("非流式任务必须提供 callback_url")

        return self

try:
    request = ChatRequest(
        message="生成一份报告",
        stream=False
    )
except ValidationError as e:
    print(e)