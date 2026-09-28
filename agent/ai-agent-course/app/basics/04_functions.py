# def greet(name):
#     return f"你好，{name}"

# result = greet("大伟")

# print(result)

def greet(name, age = 18):
    return f"你好，{name}，今年{age}岁"

print(greet("大伟"))
print(greet("大伟", 30))
print(greet("大伟", age = 30))