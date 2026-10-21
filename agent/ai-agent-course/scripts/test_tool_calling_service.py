import asyncio
import json

import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.llm.factory import LLMProviderFactory
from app.services.tool_calling_service import tool_calling_service


async def main():
    provider = LLMProviderFactory.create("deepseek")

    result = await tool_calling_service.run_with_tools(
        user_question="帮我查一下订单 10001 到哪了？",
        model="deepseek-chat",
        llm_provider=provider,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())