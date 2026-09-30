import asyncio
import time

semaphore = asyncio.Semaphore(3)

async def call_llm(index: int):
    async with semaphore:
        print(f"任务 {index} 开始调用大模型")
        await asyncio.sleep(1)
        print(f"任务 {index} 调用完成")
        return f"结果 {index}"

async def main():
    start = time.perf_counter()

    tasks = [call_llm(i) for i in range(10)]

    results = await asyncio.gather(*tasks)

    end = time.perf_counter()

    print(results)
    print(f"总耗时：{end - start:.2f} 秒")

asyncio.run(main())