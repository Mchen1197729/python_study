# 把任意的对象转换为dict类型的变量
import json


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print('Hello_Python', self.name)


s1 = Student('Jack', 20)
print(s1.__dict__)

print(json.dumps(s1, default=lambda obj: obj.__dict__))
