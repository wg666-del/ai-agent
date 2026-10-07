# import asyncio

# class AsyncDatabase:
#     async def __aenter__(self):
#         print("打开数据库连接...") # 模拟连接延迟
#         return self

#     async def __aexit__(self, exc_type, exc_value, traceback):
#         print("关闭数据库连接...") # 模拟关闭延迟

#     async def query(self, sql: str) -> str:
#         await asyncio.sleep(1)  # 模拟查询延迟
#         return f"查询结果: {sql}"

# async def main():
#     async with AsyncDatabase() as db:
#         result = await db.query("SELECT * FROM users")
#         print(result)

# asyncio.run(main())

import asyncio
import httpx

async def fetch_url(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code

async def main():
    status_code = await fetch_url("https://www.example.com")
    print(f"请求状态码: {status_code}")

asyncio.run(main())