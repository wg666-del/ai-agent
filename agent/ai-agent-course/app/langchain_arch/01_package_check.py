import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证直接运行该文件时能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from importlib.metadata import version


PACKAGES = [
    "langchain",
    "langchain-core",
    "langchain-openai",
    "langgraph"
]


def main():
    for package in PACKAGES:
        try:
            print(package, "=>", version(package))
        except Exception as exc:
            print(package, "=> 未安装", repr(exc))


if __name__ == "__main__":
    main()