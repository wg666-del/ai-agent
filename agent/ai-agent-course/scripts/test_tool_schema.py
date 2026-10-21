import json

import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.tools.registry import tool_registry


def main():
    tools = tool_registry.to_openai_tools()

    print(json.dumps(tools, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()