# from fastapi import FastAPI, Query
# from app.schemas.chat import ChatRequest, ChatResponse
# from app.services.chat_service import chat_with_ai

# app = FastAPI(
#     title="AI Agent Course API",
#     description="Python + FastAPI + LLM + Agent 开发实战",
#     version="0.1.0",
# )

# @app.get("/")
# async def root():
#     return {"message": "Hello, FastAPI!"}

# @app.get("/health")
# async def health():
#     return {"status": "ok", "service": "AI Agent Course", "version": "0.1.0"}

# @app.get("/user/{user_id}")
# async def get_user(user_id: int):
#     return {"user_id": user_id, "name": f"User {user_id}", "level": "VIP"}

# @app.get("/search")
# async def search(
#     q: str = Query(..., min_length=1, max_length=50, description="搜索关键词"),
#     page: int = Query(default=1, ge=1, description="页码"),
#     page_size: int = Query(default=10, ge=1, le=100, description="每页数量"),
# ):
#     return {
#         "query": q,
#         "page": page,
#         "page_size": page_size,
#     }

# @app.post("/chat", response_model=ChatResponse)
# async def chat(request: ChatRequest) -> ChatResponse:
#     return await chat_with_ai(request)

# from fastapi import FastAPI
# from app.api.v1.chat import router as chat_router
# from app.api.v1.health import router as health_router


# app = FastAPI(
#     title="AI Agent Course API",
#     description="Python + FastAPI + LLM + Agent 开发实战",
#     version="0.1.0",
# )

# app.include_router(health_router, prefix="/api/v1", tags=["Health"])
# app.include_router(chat_router, prefix="/api/v1", tags=["Chat"])

# @app.get("/")
# async def root():
#     return {"message": "Hello, FastAPI!"}

from fastapi import FastAPI
from app.api.v1.chat import router as chat_router
from app.api.v1.health import router as health_router
from app.api.v1.conversations import router as conversations_router
from app.api.v1.rag import router as rag_router

app = FastAPI(
    title="AI Agent Course API",
    description="Python + FastAPI + LLM + Agent 开发实战",
    version="0.1.0",
)

app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(chat_router, prefix="/api/v1", tags=["Chat"])
app.include_router(conversations_router, prefix="/api/v1", tags=["Conversations"])
app.include_router(rag_router, prefix="/api/v1", tags=["RAG"])

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
