from typing import Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    code: int = Field(default=0, description="响应状态码")
    message: str = Field(default="success", description="响应消息")
    data: T | None = Field(default=None, description="响应数据")
    trace_id: str | None = Field(default=None, description="链路追踪 ID")

class ErrorDetail(BaseModel):
    field: str | None = Field(default=None, description="错误字段")
    message: str = Field(..., description="错误信息")

class ErrorResponse(BaseModel):
    code: int = Field(default=500, description="错误码")
    message: str = Field(..., description="错误信息")
    data: dict | list | None = Field(default=None, description="错误数据")
    trace_id: str | None = Field(default=None, description="链路追踪 ID")