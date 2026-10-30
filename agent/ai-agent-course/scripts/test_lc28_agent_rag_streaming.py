import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.langchain_agent_rag.demo_agent_rag_streaming import main

import asyncio

if __name__ == "__main__":
    asyncio.run(main())