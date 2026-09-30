# import asyncio


# async def call_llm():
#     print("开始调用大模型")
#     await asyncio.sleep(5)
#     return "AI 回答"

# async def main():
#     try:
#         result = await asyncio.wait_for(
#             call_llm(),
#             timeout=2
#         )
#         print(result)
#     except asyncio.TimeoutError:
#         print("大模型调用超时")

# asyncio.run(main())

import asyncio


async def call_advanced_model():
    print("调用高级模型")
    await asyncio.sleep(5)
    return "高级模型回答"


async def call_backup_model():
    print("调用备用模型")
    await asyncio.sleep(1)
    return "备用模型回答"


async def main():
    try:
        result = await asyncio.wait_for(
            call_advanced_model(),
            timeout=2
        )
    except asyncio.TimeoutError:
        print("高级模型超时，切换备用模型")
        result = await call_backup_model()

    print(result)


asyncio.run(main())