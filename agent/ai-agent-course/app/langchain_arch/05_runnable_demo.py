import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证直接运行该文件时能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from langchain_core.runnables import RunnableLambda

def add_one(x: int) -> int:
    return x + 1


def multiply_two(x: int) -> int:
    return x * 2


def main():
    add_one_runnable = RunnableLambda(add_one)
    multiply_two_runnable = RunnableLambda(multiply_two)

    chain = add_one_runnable | multiply_two_runnable

    result = chain.invoke(10)

    print("result:", result)


if __name__ == "__main__":
    main()