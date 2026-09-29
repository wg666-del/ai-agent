# def divide(a: int, b: int) -> float:
#     return a / b

# try:
#     result = divide(10, 0)
#     print(result)
# except ZeroDivisionError as e:
#     print(f"除数不能为0：{e}")
# except Exception as e:
#     print(f"其他错误：{e}")
# finally:
#     print("不管有没有报错，finally 都会执行")

class ModelNotFoundError(Exception):
    pass

def get_model(model_name: str) -> str:
    supported_models = ["deepseek-chat", "qwen-plus", "gpt-4o-mini"]

    if model_name not in supported_models:
        raise ModelNotFoundError(f"不支持的模型：{model_name}")

    return model_name

try:
    model = get_model("unknown-model")
    print(model)
except ModelNotFoundError as e:
    print(f"模型错误：{e}")