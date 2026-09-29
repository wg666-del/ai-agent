# def get_user_name(user_id: int) -> int | None:
#     if user_id == 1:
#         return "大伟"

#     return None

# print(get_user_name(1))
# print(get_user_name(2))

# from pydantic import BaseModel

# class UserA(BaseModel):
#     name: str
#     email: str | None

# class UserB(BaseModel):
#     name: str
#     email: str | None = None

# print(UserB(name="大伟").model_dump())

def parse_id(value: int | str) -> str:
    return str(value)

print(parse_id(10001))
print(parse_id("10001"))