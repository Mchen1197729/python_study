# 在python中定义函数
def greet(name):
    print('Hello,%s!Welcome to my page!Hope you will enjoy it.' % name)


greet('Jack')


def _abs(number):
    if not isinstance(number, (int, float)):
        return 'TypeError'
    if number >= 0:
        return number
    else:
        return -number


print(_abs(100))
print(_abs('123'))

print('**************返回多个值***************')


# 如果函数没有显式的声明return返回值 那么函数运行到末尾时会隐式的调用return None

# 如果函数中返回值是多个 那么最终会被包装成一个tuple对象
def test():
    return 100, 200, 300


print(test())
