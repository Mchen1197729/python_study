import functools

# python中的偏函数:本质就是创建一个新的函数 而这个函数固定住了原来函数的部分参数 使得函数的调用变得更简单了

# 将字符串转换成数值类型
balance = '100'
print(int(balance))  # 默认是十进制的
print(int(balance, base=2))  # 可以指定base关键字参数来按照指定的进制进行转换
print(int(balance, base=3))
print(int(balance, 8))  # base关键字可以省略


# 可以自定义一个函数用来指明按照某种进制进行转换
def int8(x, base=8):
    return int(x, base)  # 此处省略了base关键字


print(int8(balance))
print(int8(balance, base=18))

# 可以使用python提供的functools.partial()工具函数来创建一个偏函数
int18 = functools.partial(int, base=18)

print(int18(balance))
print(int18(balance, base=2))

print(max(1, 2, 3, 4))

# functools.partial(func,*args,**kw) === return func(*args,**kw)
max10 = functools.partial(max, 10)
print(max10(9, 9, 7))


def my_sum(*args):
    return sum(args)


my_sum12 = functools.partial(my_sum, 1, 2)
print(my_sum12(3, 4, 5))
