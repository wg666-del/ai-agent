import asyncio
import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


import asyncio
import json

from app.langchain_tools.service import langchain_tool_calling_service


async def main():
    result = await langchain_tool_calling_service.run_ecommerce_customer_service(
        user_question="帮我查一下订单 10001 到哪了？",
        provider="deepseek",
        model_name="deepseek-chat",
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())