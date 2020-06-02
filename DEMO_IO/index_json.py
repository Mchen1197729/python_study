# 使用json模块进行序列化和反序列化
import json

stu = dict(name='林志玲', age=49, gender='female')
print(json.dumps(stu))  # {"name": "\u6797\u5fd7\u73b2", "age": 49, "gender": "female"}

arr = list([1, 2, 3, 4, 5, '刘德华'])
print(json.dumps(arr))  # [1, 2, 3, 4, 5, "\u5218\u5fb7\u534e"]

# 将序列化的内容写入指定的文件
with open('./json/stu.json', 'w') as fj:
    json.dump(stu, fj, ensure_ascii=True)

with open('./json/arr.json', 'w') as fj1:
    json.dump(arr, fj1)

# 将json文件中的内容读反序列化到内存中
with open('./json/stu.json', 'r') as fjr:
    print(json.load(fjr))

# with open('./json/arr.json', 'r') as fjr2:
#     print(json.loads(fjr2))

print('************************')


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


print(json.dumps(Student('Rose', 22), default=lambda x: x.__dict__))
print(json.dumps(Student('Rose', 22).__dict__))


def dict2student(d):
    return Student(d['name'], d['age'])


json_stu = '{"age": 20, "name": "Bob"}'

print(json.loads(json_stu, object_hook=dict2student))

print('******************')

obj = dict(name='小明', age=20)
s1 = json.dumps(obj, ensure_ascii=False)
s2 = json.dumps(obj, ensure_ascii=True)
print(s1, s2)
