import asyncio
import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.db.init_db import init_db

async def main():
    await init_db()
    print("数据库表创建完成")

if __name__ == "__main__":
    asyncio.run(main())