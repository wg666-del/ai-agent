# name = "大伟"
# age = 18
# score = 99.5
# is_teacher = True
# nothing = None

# user_name = "张三"
# max_retry_count = 3
# is_login = False

# msg2 = f"你好，我是{name}，今年{age}岁"

# fruits = ["苹果", "香蕉", "橙子"]

# fruits.append("葡萄")
# fruits[0] = "西瓜"
# fruits.remove("香蕉")

# for fruit in fruits:
#     print(fruit)

# print(name)
# print(age)
# print(score)
# print(is_teacher)
# print(nothing)

# print(user_name)
# print(max_retry_count)
# print(is_login)

# print(msg2)

# print("年龄：" + str(age))
# print(f"年龄：{age}")

# print(fruits)
# print(fruits[0])
# print(fruits[-1])

# print(fruits)
# print(len(fruits))

numbers = [1, 2, 3, 4, 5]

result = []

for num in numbers:
    result.append(num * 2)

print(result)

doubled = [num * 2 for num in numbers]

print(doubled)

big_numbers = [num for num in numbers if num > 2]

print(big_numbers)

print([num * 2 for num in numbers if num > 2])