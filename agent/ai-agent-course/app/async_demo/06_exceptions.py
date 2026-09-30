# import asyncio


# async def query_order():
#     await asyncio.sleep(1)
#     raise ValueError("订单服务异常")


# async def main():
#     try:
#         result = await query_order()
#         print(result)
#     except ValueError as e:
#         print(f"捕获异常：{e}")


# asyncio.run(main())

# import asyncio


# async def query_order():
#     await asyncio.sleep(1)
#     raise ValueError("订单服务异常")


# async def query_user():
#     await asyncio.sleep(1)
#     return "用户信息"


# async def main():
#     try:
#         results = await asyncio.gather(
#             query_order(),
#             query_user()
#         )
#         print(results)
#     except Exception as e:
#         print(f"gather 捕获异常：{e}")


# asyncio.run(main())


import asyncio


async def query_order():
    await asyncio.sleep(1)
    raise ValueError("订单服务异常")


async def query_user():
    await asyncio.sleep(1)
    return "用户信息"

async def main():
    results = await asyncio.gather(
        query_order(),
        query_user(),
        return_exceptions=True
    )

    for result in results:
        if isinstance(result, Exception):
            print(f"任务失败：{result}")
        else:
            print(f"任务成功：{result}")

asyncio.run(main())