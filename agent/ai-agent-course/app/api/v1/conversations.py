from fastapi import APIRouter, Path, Depends

from app.dependencies.database import MockBDSession, get_db_session

from app.dependencies.pagination import PaginationParams

from app.schemas.conversation import (
    ConversationCreateRequest,
    ConversationMessagesResponse,
    ConversationResponse,
)
from app.schemas.response import ApiResponse
from app.services.conversation_service import (
    create_conversation,
    get_conversation_messages,
)

router = APIRouter()


@router.post("/conversations", response_model=ApiResponse[ConversationResponse])
async def create_new_conversation(
    request: ConversationCreateRequest,
    db: MockBDSession = Depends(get_db_session)
) -> ApiResponse[ConversationResponse]:
    sql_result = await db.execute("INSERT INTO conversations ...")
    print(sql_result)

    result = await create_conversation(request)

    return ApiResponse[ConversationResponse](
        data=result
    )


@router.get(
    "/conversations/{conversation_id}/messages",
    response_model=ApiResponse[ConversationMessagesResponse],
)
async def get_messages(
    conversation_id: str = Path(..., description="会话 ID"),
) -> ApiResponse[ConversationMessagesResponse]:
    result = await get_conversation_messages(conversation_id)

    return ApiResponse[ConversationMessagesResponse](
        data=result
    )


@router.get("/conversations", response_model=ApiResponse[dict])
async def list_conversations(
    pagination: PaginationParams = Depends(PaginationParams),
) -> ApiResponse[dict]:
  return ApiResponse[dict](
     data={
        "page": pagination.page,
          "page_size": pagination.page_size,
          "offset": pagination.offset,
          "items": [],
     }
  )