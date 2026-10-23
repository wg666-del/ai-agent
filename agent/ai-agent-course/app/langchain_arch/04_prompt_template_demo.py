import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证直接运行该文件时能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


from langchain_core.prompts import ChatPromptTemplate


def main():
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            (
                "你是一个专业的 {role_name}。\n"
                "回答要求：\n"
                "1. 使用中文。\n"
                "2. 结构清晰。\n"
                "3. 不要编造。"
            ),
        ),
        (
            "human",
            "用户问题：{question}",
        ),
    ])

    prompt_value = prompt.invoke({
        "role_name": "AI Agent 课程助教",
        "question": "LangChain PromptTemplate 解决什么问题？",
    })

    print("prompt value type:", type(prompt_value))
    print("messages:")

    for message in prompt_value.messages:
        print(message.type, ":", message.content)
        print("-" * 60)


if __name__ == "__main__":
    main()