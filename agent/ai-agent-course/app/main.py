from fastapi import FastAPI

app = FastAPI(
    title="AI Agent 全栈开发实战",
    description="Python + FastAPI + LLM + Agent",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "Hello AI Agent"
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "ai-agent-course",
    }