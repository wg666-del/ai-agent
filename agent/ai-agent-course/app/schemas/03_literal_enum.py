# from typing import Literal

# modelName = Literal["deepseek-chat", "qwen-plus", "gpt-4o-mini"]

# def chat(message: str, model: modelName) -> str:
#     return f"使用 {model} 回答：{message}"

# print(chat("什么是 AI Agent？", "deepseek-chat"))

from enum import Enum

class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

def create_message(role: MessageRole, content: str) -> dict[str, str]:
    return {
        "role": role.value,
        "content": content
    }

print(create_message(MessageRole.USER, "你好"))