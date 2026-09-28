user = {
    "name": "大伟",
    "age": 30,
    "city": "北京"
}

# print(user)
# print(user["name"])
# print(user["city"])

# print(user.get("name"))
# print(user.get("email"))
# print(user.get("email", "未填写"))

for key, value in user.items():
    print(f"{key}: {value}")