import asyncio

import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.llm.providers.deepseek import DeepSeekProvider
from app.llm.schemas import LLMMessage, LLMRequest, LLMRole


async def main():
  provider = DeepSeekProvider()

  request = LLMRequest(
    model="deepseek-chat",
    messages=[
      LLMMessage(
        role=LLMRole.USER,
        content="请用三句话解释为什么要封装 LLM Provider。"
      )
    ],
    temperature=0.7,
    stream=True,
  )

  full_content = ""

  async for chunk in provider.stream_chat(request):
    if chunk.content:
      full_content += chunk.content
      print(chunk.content, end="", flush=True)

    if chunk.usage:
      print("\nusage:", chunk.usage.model_dump())

  print("\n\nfull_content:")
  print(full_content)

if __name__ == "__main__":
  asyncio.run(main())