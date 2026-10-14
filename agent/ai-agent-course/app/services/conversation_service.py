from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.conversation_repository import conversation_repository
from app.schemas.conversation import (
    ConversationCreateRequest,
    ConversationMessagesResponse,
    ConversationResponse,
)

from redis.asyncio import Redis

from app.redis.cache import (
    cache_recent_messages,
    get_cached_recent_messages,
)


async def create_conversation(
    db: AsyncSession,
    request: ConversationCreateRequest,
    user_id: str | None = None,
) -> ConversationResponse:
    conversation = await conversation_repository.create(
        db=db,
        request=request,
        user_id=user_id,
    )

    return ConversationResponse(
        conversation_id=conversation.id,
        title=conversation.title,
        status=conversation.status,
        created_at=conversation.created_at,
        updated_at=conversation.updated_at,
    )


async def get_conversation_messages(
    db: AsyncSession,
    conversation_id: str,
    redis: Redis | None = None,
) -> ConversationMessagesResponse:
    if redis:
        cached_messages = await get_cached_recent_messages(
            redis=redis,
            conversation_id=conversation_id
        )

        if cached_messages is not None:
            return ConversationMessagesResponse(
                conversation_id=conversation_id,
                messages=cached_messages,
            )

    
    messages = await conversation_repository.get_messages(
        db=db,
        conversation_id=conversation_id,
    )

    if redis:
        await cache_recent_messages(
            redis=redis,
            conversation_id=conversation_id,
            messages=messages[-10:]
        )

    return ConversationMessagesResponse(
        conversation_id=conversation_id,
        messages=messages,
    )