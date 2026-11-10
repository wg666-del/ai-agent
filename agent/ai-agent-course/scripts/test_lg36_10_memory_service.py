import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.langgraph_memory.service import langgraph_memory_service


def main():
    tenant_id = "tenant_001"
    user_id = "u_10001"
    conversation_id = "conv_memory_001"

    first = langgraph_memory_service.chat(
        tenant_id=tenant_id,
        user_id=user_id,
        conversation_id=conversation_id,
        question="记住：以后回答客服问题，先给结论，再给处理步骤。",
    )

    print("first:")
    print(first)
    print("=" * 80)

    second = langgraph_memory_service.chat(
        tenant_id=tenant_id,
        user_id=user_id,
        conversation_id=conversation_id,
        question="你记得我的偏好吗？",
    )

    print("second:")
    print(second)
    print("=" * 80)

    memories = langgraph_memory_service.list_memories(
        tenant_id=tenant_id,
        user_id=user_id,
    )

    print("memories:")
    for memory in memories:
        print(memory)


if __name__ == "__main__":
    main()