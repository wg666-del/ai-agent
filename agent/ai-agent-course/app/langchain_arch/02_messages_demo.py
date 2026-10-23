import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证直接运行该文件时能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    ToolMessage,
    AIMessage,
)


def main():
    messages = [
        SystemMessage(content="你是一个专业 AI Agent 课程助教。"),
        HumanMessage(content="请解释 LangChain Message 的作用。"),
        AIMessage(content="Message 是对大模型对话消息的对象化封装。"),
        ToolMessage(
            content='{"order_id":"10001", "status":"已发货"}',
            tool_call_id="call_query_order_001",
        ),
    ]

    for message in messages:
        print("type:", message.type)
        print("content:", message.content)
        print("dict:", message.model_dump())
        print("=" * 80)


if __name__ == "__main__":
    main()