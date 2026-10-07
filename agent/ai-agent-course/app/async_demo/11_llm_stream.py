# import asyncio
# from collections.abc import AsyncGenerator

# async def fake_llm_stream(prompt: str) -> AsyncGenerator[str, None]:
#     answer = f"根据你的问题 {prompt}， AI agent是能够理解目标、规划步骤并调用工具完成任务的智能体。"
#     for char in answer:
#         await asyncio.sleep(0.1)  # 模拟生成每个字符的延迟
#         yield char

# async def main():
#     async for token in fake_llm_stream("什么是AI agent？"):
#         print(token, end='', flush=True)  # 实时输出每个字符

#     print()  # 换行

# asyncio.run(main())


import asyncio
from collections.abc import AsyncGenerator

async def fake_llm_stream(prompt: str) -> AsyncGenerator[str, None]:
    answer = f"根据你的问题 {prompt}， AI agent是能够理解目标、规划步骤并调用工具完成任务的智能体。"
    for char in answer:
        await asyncio.sleep(0.1)  # 模拟生成每个字符的延迟
        yield {
            "type": "token",
            "content": char
        }

    yield {
        "type": "done",
        "content": ""
    }

async def main():
    async for chunk in fake_llm_stream("什么是AI agent？"):
        if chunk["type"] == "token":
            print(chunk["content"], end='', flush=True)  # 实时输出每个字符
        elif chunk["type"] == "done":
            print("\n流式输出完成。")  # 输出完成标志

asyncio.run(main())