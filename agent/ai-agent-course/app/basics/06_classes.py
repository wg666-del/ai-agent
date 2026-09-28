# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def greet(self) -> str:
#         return f"我是 {self.name}，今年 {self.age} 岁"

# user = User("大伟", 30)

# print(user.name)
# print(user.age)
# print(user.greet())

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def greet(self) -> str:
        return f"我是{self.name},今年{self.age}岁"

class Teacher(User):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject
    def introduce(self) -> str:
        return f"我是{self.name},我教{self.subject}"

teacher = Teacher("大伟", 30, "AI Agent 开发")

print(teacher.greet())
print(teacher.introduce())