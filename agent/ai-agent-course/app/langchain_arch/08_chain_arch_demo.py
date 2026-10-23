import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证直接运行该文件时能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))



from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from app.core.config import settings


def create_model():
    return ChatOpenAI(
        model="deepseek-chat",
        api_key=settings.deepseek_api_key,
        base_url=settings.deepseek_base_url,
        temperature=0.7,
    )


def add_prefix(text: str) -> str:
    return f"【LangChain 架构解释】\n{text}"


def main():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业 AI Agent 课程助教。"),
        ("human", "请用三句话解释：{topic}"),
    ])

    model = create_model()
    parser = StrOutputParser()
    prefix = RunnableLambda(add_prefix)

    chain = prompt | model | parser | prefix

    result = chain.invoke({
        "topic": "Runnable 为什么是 LangChain 的核心",
    })

    print(result)


if __name__ == "__main__":
    main()