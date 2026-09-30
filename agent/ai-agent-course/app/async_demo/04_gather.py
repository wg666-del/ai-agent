import asyncio


async def task_a():
    await asyncio.sleep(2)
    return "A"


async def task_b():
    await asyncio.sleep(1)
    return "B"


async def task_c():
    await asyncio.sleep(0.5)
    return "C"


async def main():
    results = await asyncio.gather(
        task_a(),
        task_b(),
        task_c()
    )

    print(results)


asyncio.run(main())