# import asyncio

# async def fetch_data():
#     print("开始获取数据")
#     await asyncio.sleep(1)
#     print("获取数据完成")
#     return "这是数据"

# result = asyncio.run(fetch_data())

# print(result)

# import asyncio

# async def query_user():
#     await asyncio.sleep(1)
#     return "用户信息"

# async def query_order():
#     await asyncio.sleep(1)
#     return "订单信息"

# async def query_llm():
#     await asyncio.sleep(1)
#     return "AI 回答"

# async def main():
#     user, order, answer = await asyncio.gather(
#         query_user(),
#         query_order(),
#         query_llm()
#     )

#     print(user)
#     print(order)
#     print(answer)

# asyncio.run(main())


# import asyncio

# async def generate_tokens():
#     tokens = ["你", "好", "，", "我", "是", "AI", "。"]

#     for token in tokens:
#         await asyncio.sleep(0.2)
#         yield token

# async def main():
#     async for token in generate_tokens():
#         print(token, end="", flush=True)

#     print()

# asyncio.run(main())

import asyncio

class AsyncDataBase:
    async def __aenter__(self):
        print("打开数据库连接")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("关闭数据库连接")

    async def query(self, sql: str) -> str:
        print("查询中，请稍后...")
        await asyncio.sleep(1)
        return f"查询结果：{sql}"

async def main():
    async with AsyncDataBase() as db:
        result = await db.query("SELECT * FROM users")
        print(result)

asyncio.run(main())