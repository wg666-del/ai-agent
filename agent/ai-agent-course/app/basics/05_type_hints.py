# def add(a: int, b :int) -> int:
#     return a + b

# result = add(1, 2)

# print(result)
# print(add("1", "2"))

# from typing import Any

# name: str = "大伟"
# age: int = 30
# score: float = 99.5
# is_active: bool = True
# tags: list[str] = ["AI", "FastAPI", "Agent"]
# user: dict[str, Any] = {
#     "name": "大伟",
#     "age": 30
# }

# print(name)
# print(tags)
# print(user)

def get_user_name(user_id: int) -> str | None:
    if user_id == 1:
        return "大伟"
    return None

print(get_user_name(user_id=1))
print(get_user_name(user_id=2))
