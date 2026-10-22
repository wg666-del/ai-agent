import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证直接运行该文件时能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from app.core.config import settings


def create_deepseek_chat_model():
    if not settings.deepseek_api_key:
        raise RuntimeError("请先在 .env 中配置 DEEPSEEK_API_KEY")

    return ChatOpenAI(
        model="deepseek-chat",
        api_key=settings.deepseek_api_key,
        base_url=settings.deepseek_base_url,
        temperature=0.7,
    )


def run_basic_chat():
    model = create_deepseek_chat_model()

    response = model.invoke("请用一句话解释什么是 LangChain。")

    print("response type:", type(response))
    print("content:")
    print(response.content)

def run_chat_with_messages():
    model = create_deepseek_chat_model()

    messages = [
        SystemMessage(content="你是一个专业 AI Agent 课程助教。"),
    ]


if __name__ == "__main__":
    run_basic_chat()