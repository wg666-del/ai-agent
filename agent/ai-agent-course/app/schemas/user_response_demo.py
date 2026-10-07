from pydantic import BaseModel

class UserInDB(BaseModel):
    user_id: str
    username: str
    email: str
    password_hash: str

class UserResponse(BaseModel):
    user_id: str
    username: str
    email: str

user = UserInDB(
    user_id="u_10001",
    username="dawei",
    email="dawei@example.com",
    password_hash="hashed_password_xxx"
)

response = UserResponse(
    user_id=user.user_id,
    username=user.username,
    email=user.email
)

print(response.model_dump())