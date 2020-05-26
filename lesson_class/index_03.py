# 获取对象的类型
print(type(11))  # <class 'int'>
print(type('abc'))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({'name': 'Jack'}))  # <class 'dict'>
print(type(object))  # <class 'type'>
print(type(type(abs)))  # <class 'type'>

print(type(111) == "<class 'int'>")  # False
print(type(111) == int)  # True
print(type('111') == str)  # True
print(type([1, 2, 3]) == list)  # True
print(type((1, 2, 3)) == tuple)  # True
print(type({'name': 'Jack'}) == dict)  # True

# 如果一个变量是函数类型 也乐意用type()来判断
print(type(abs))
print(type(type(abs)) == type)  # True
