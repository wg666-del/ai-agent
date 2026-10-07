# import asyncio

# async def generate_numbers():
#     for i in range(5):
#         await asyncio.sleep(1)
#         yield i

# async def main():
#     async for num in generate_numbers():
#         print(f"生成的数字: {num}") 

# asyncio.run(main())

import asyncio

async def stream_llm_answer(question: str):
    answer = f"你问的是：{question}。这是一个模拟的流式回答。"

    for char in answer:
        await asyncio.sleep(0.1)  # 模拟生成每个字符的延迟
        yield char

async def main():
    async for chunk in stream_llm_answer("什么是异步生成器？"):
        print(chunk, end='', flush=True)  # 实时输出每个字符

    print()  # 换行

asyncio.run(main())