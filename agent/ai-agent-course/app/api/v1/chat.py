from fastapi import APIRouter, Path, Query, Body

from app.schemas.chat import ChatRequest, ChatResponse, GenerateTitleRequest, GenerateTitleResponse
from app.schemas.response import ApiResponse
from app.services.chat_service import chat_with_ai

router = APIRouter()


@router.post("/chat", response_model=ApiResponse[ChatResponse])
async def chat(request: ChatRequest) -> ApiResponse[ChatResponse]:
    result = await chat_with_ai(request)

    return ApiResponse[ChatResponse](
        data=result
    )

@router.post("/conversations/{conversation_id}/chat", response_model=ApiResponse[ChatResponse])
async def chat_in_conversation(
    request: ChatRequest,
    conversation_id: str = Path(..., description="会话 ID"),
    debug: bool = Query(default=False, description="是否开启调试模式"),
) -> ApiResponse[ChatResponse]:
    result = await chat_with_ai(request)

    if debug:
        result.trace_id = result.trace_id or "debug_trace"

    result.session_id = conversation_id

    return ApiResponse[ChatResponse](
        data=result
    )

@router.post("/chat/title", response_model=ApiResponse[GenerateTitleResponse])
async def generate_chat_title(
    request: GenerateTitleRequest,
) -> ApiResponse[GenerateTitleResponse]:
    title = request.message[:20]

    return ApiResponse[GenerateTitleResponse](
        data=GenerateTitleResponse(title=title)
    )