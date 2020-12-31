# 在python中格式化字符串
print('我是{},我今年{}岁，我来自{}'.format('刘德华', 60, '香港'))

print('我是{name},我今年{age}岁，我来自{address}'.format(name='刘德华', age=60, address='香港'))

person = {"name": "刘德华", "age": 60, "address": "香港"}
print('我是{name},我今年{age}岁，我来自{address}'.format(**person))

p = ["刘德华", 60, "香港"]
print('我是{},我今年{}岁，我来自{}'.format(*p))

# print(**person)
print(*p)
print([*p])
print({*p})
print({**person})
