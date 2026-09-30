import time


def query_user():
    print("开始查询用户信息")
    time.sleep(1)
    print("用户信息查询完成")
    return "用户信息"


def query_order():
    print("开始查询订单信息")
    time.sleep(1)
    print("订单信息查询完成")
    return "订单信息"


def query_llm():
    print("开始调用大模型")
    time.sleep(2)
    print("大模型返回结果")
    return "AI 回答"


def main():
    start = time.perf_counter()

    user = query_user()
    order = query_order()
    answer = query_llm()

    end = time.perf_counter()

    print(user)
    print(order)
    print(answer)
    print(f"总耗时：{end - start:.2f} 秒")


main()