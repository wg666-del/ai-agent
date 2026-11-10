import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.langgraph_multi_agent.service import langgraph_multi_agent_service


def main():
    ecommerce_result = langgraph_multi_agent_service.chat(
        question="我的订单 10002 可以退款吗？",
        graph_type="ecommerce",
    )

    print("ecommerce_result:")
    print(ecommerce_result)
    print("=" * 120)

    data_result = langgraph_multi_agent_service.chat(
        question="帮我分析最近 30 天销售数据。",
        graph_type="data_analysis",
    )

    print("data_result:")
    print(data_result)


if __name__ == "__main__":
    main()