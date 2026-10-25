import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.langchain_models.message_adapter import to_langchain_messages
from app.llm.schemas import LLMMessage, LLMRole


def main():
    messages = [
        LLMMessage(
            role=LLMRole.SYSTEM,
            content="你是一个专业 AI Agent 课程助教。",
        ),
        LLMMessage(
            role=LLMRole.USER,
            content="请解释 MessageAdapter 的作用。",
        ),
    ]

    langchain_messages = to_langchain_messages(messages)

    for message in langchain_messages:
        print(message.__class__.__name__)
        print(message.type)
        print(message.content)
        print("=" * 80)


if __name__ == "__main__":
    main()