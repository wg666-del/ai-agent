# def add(a: int, b: int) -> int:
#     return a + b

# # result = add(1, 2)
# result = add("1", "2")

# print(result)

from typing import Any

name: str = "大伟"
age: int = 30
score: float = 99.5
is_active: bool = True
extra: Any = {"level": "senior"}

tags: list[str] = ["Python", "FastAPI", "Agent"]

user: dict[str, Any] = {
    "name": "大伟",
    "age": 30,
    "city": "北京"
}

print(name)
print(age)
print(score)
print(is_active)
print(extra)
print(tags)
print(user)