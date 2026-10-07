import asyncio
import time
from typing import Any
from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    user_id: str = Field(..., description="用户ID")
    order_id: str = Field(..., description="订单ID")
    question: str = Field(..., description="用户问题")

async def query_user(user_id: str) -> dict[str, Any]:
    print("开始查询用户信息...")
    await asyncio.sleep(1)  # 模拟查询延迟
    print("用户信息查询完成")

    return {
        "user_id": user_id,
        "name": "大伟",
        "level": "VIP"
    }

async def query_order(order_id: str) -> dict[str, Any]:
    print("开始查询订单信息")
    await asyncio.sleep(1)
    print("订单信息查询完成")

    return {
        "order_id": order_id,
        "status": "已发货",
        "amount": 299
    }


async def query_logistics(order_id: str) -> dict[str, Any]:
    print("开始查询物流信息")
    await asyncio.sleep(2)
    print("物流信息查询完成")

    return {
        "order_id": order_id,
        "company": "顺丰",
        "status": "运输中",
        "eta": "明天送达"
    }

async def call_llm(
    question: str,
    user: dict[str, Any],
    order: dict[str, Any],
    logistics: dict[str, Any]
) -> str:
    print("开始调用大模型生成最终回答")
    await asyncio.sleep(1)

    return (
        f"用户 {user['name']}，您的订单 {order['order_id']} 当前状态是"
        f"{order['status']}，物流公司是{logistics['company']}，"
        f"当前物流状态：{logistics['status']}，预计{logistics['eta']}。"
    )

async def agent_run(request: AgentRequest) -> str:
    user, order, logistics = await asyncio.gather(
        safe_call_tool("查询用户信息", query_user(request.user_id)),
        safe_call_tool("查询订单信息", query_order(request.order_id)),
        safe_call_tool("查询物流信息", query_logistics(request.order_id))
    )

    answer = await call_llm(
        question=request.question,
        user=user,
        order=order,
        logistics=logistics
    )

    return answer

async def main():
    start = time.perf_counter()

    request = AgentRequest(
        user_id="u_10001",
        order_id="o_10001",
        question="帮我查询一下订单物流状态"
    )

    answer = await agent_run(request)

    end = time.perf_counter()

    print(answer)
    print(f"总耗时：{end - start:.2f} 秒")


async def safe_call_tool(tool_name: str, coro, timeout: float = 2):
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        return {
            "error": f"{tool_name} 调用超时"
        }
    except Exception as e:
        return {
            "error": f"{tool_name} 调用失败: {e}"
        }


asyncio.run(main())



