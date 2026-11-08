import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.langgraph_hitl.service import langgraph_hitl_service


def main():
    tenant_id = "tenant_001"
    user_id = "u_10001"
    conversation_id = "conv_hitl_refund_001"

    first = langgraph_hitl_service.start(
        user_question="我的订单 10003 申请退款。",
        tenant_id=tenant_id,
        user_id=user_id,
        conversation_id=conversation_id,
    )

    print("first:")
    print(first)

    print("=" * 80)

    state = langgraph_hitl_service.get_state(
        tenant_id=tenant_id,
        user_id=user_id,
        conversation_id=conversation_id,
    )

    print("state before resume:")
    print(state["values"])

    print("=" * 80)

    second = langgraph_hitl_service.resume(
        tenant_id=tenant_id,
        user_id=user_id,
        conversation_id=conversation_id,
        decision={
            "type": "approve",
            "reviewer_id": "admin_001",
            "reason": "审核通过",
        },
    )

    print("second:")
    print(second)


if __name__ == "__main__":
    main()