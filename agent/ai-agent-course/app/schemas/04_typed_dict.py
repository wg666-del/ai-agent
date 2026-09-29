from typing import TypedDict

class MessageDict(TypedDict):
    role: str
    content: str

message: MessageDict = {
    "role": "user",
    "content": "你好"
}

print(message)