import asyncio
import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.tools.executor import tool_executor


async def main():
    result = await tool_executor.execute(
        tool_name="query_order",
        arguments={
            "order_id": "10001",
        },
    )

    print(result.model_dump())

    result = await tool_executor.execute(
        tool_name="query_logistics",
        arguments={
            "tracking_no": "SF10001",
        },
    )

    print(result.model_dump())


if __name__ == "__main__":
    asyncio.run(main())