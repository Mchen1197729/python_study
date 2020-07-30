# Python中的偏函数

# int(number,**01_base=10) 进行指定进制的转换（默认是十进制）
import functools

print(int('12345'))
print(int('12345', base=16))

print(int('10', 2))


def int2sixteen(n):
    return int(n, base=16)


print(int2sixteen('100'))
print(int2sixteen('12345'))


def int2(n, base=2):
    return int(n, base)


print(int2('1010'))

print('*********************')
# 使用functools.partial()创建一个偏函数
int8 = functools.partial(int, base=8)


def say(name='tom'):
    print(name)


say_jerry = functools.partial(say, name='jerry')
say_jerry()

print('*********************')
max10 = functools.partial(max, 10)
print(max10(11, 2, 3, 9))

print('*********************')


def why(*args, **kwargs):
    print(args, kwargs)


why_partial = functools.partial(why, 1, 2, 3, 4, 5, name='Tom', age=28, married=False)

why_partial()
