import asyncio

async def stream_llm_answer(message: str):
    answer = f"这是针对 {message} 的模拟 AI 流式回答。"

    for char in answer:
        await asyncio.sleep(0.05)
        yield char

async def main():
    async for chunk in stream_llm_answer("什么是 RAG？"):
        print(chunk, end="", flush=True)

    print()

asyncio.run(main())