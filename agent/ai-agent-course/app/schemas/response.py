from typing import Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    code: int = Field(default=0, description="响应状态码")
    message: str = Field(default="success", description="响应消息")
    data: T | None = Field(default=None, description="响应数据")

class ErrorResponse(BaseModel):
    code: int = Field(default=500, description="错误码")
    message: str = Field(..., description="错误信息")
    detail: str | None = Field(default=None, description="错误详情")