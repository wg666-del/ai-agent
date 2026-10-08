import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证以脚本方式（python tests/xxx.py）运行也能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.schemas.chat import ChatMessage, ChatRequest, MessageRole


request = ChatRequest(
    messages=[
        ChatMessage(
            role=MessageRole.SYSTEM,
            content="你是一个专业 AI 助手"
        ),
        ChatMessage(
            role=MessageRole.USER,
            content="什么是 AI Agent？"
        )
    ],
    model="deepseek-chat",
    temperature=0.7,
    stream=False,
)

print(request.model_dump())