# python中有许多内置函数 比如：转换数据类型的函数

# 1.将字符串转换为int&float类型
print(int('123') + 1)
print(float('123.45') + 1)

# 2.将数值转换为str类型
print(str(123) + 'abc')

# 3.将其他类型转换成bool类型:一般只要是没有意义的值都会被转成False
print(bool(123))
print(bool('0'))
# 下面的都会被转换成False
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(None))
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(range(0)))
print(bool(set()))
