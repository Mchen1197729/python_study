# 在python中 lambda关键字表示匿名函数
# lambda函数只能有一个表达式作为函数体 该表达式的结果作为该匿名函数的返回值

# reduce&filter&map函数的第一个参数都是处理函数 第二个参数才是列表对象
# sorted函数第一个参数是列表对象 接下来的参数才是命名关键字参数(key:Function,reverse:bool)
from functools import reduce

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选出所有的偶数
print(list(filter(lambda x: x % 2 == 0, numbers)))

# 返回每个数的平方组成的新列表
print(list(map(lambda x: x ** 2, numbers)))

# 返回按照降序排列的新的列表
print(list(sorted(numbers, key=lambda x: -x)))
# 或者
print(list(sorted(numbers, key=lambda x: x, reverse=True)))

# 求和
print(reduce(lambda x, y: x + y, numbers))


def f1(args):
    print('f1被调用')
    return args + 'f1-'


def f2(args):
    print('f2被调用')
    return args + 'f2-'


def f3(args):
    print('f3被调用')
    return args + 'f3-'


def f4(args):
    print('f4被调用')
    return args + 'f4-'


funcs = [f1, f2, f3, f4]

fn = reduce(lambda a, b: lambda args='': a(b(args)), funcs)
print(fn())

print('*******************************')
L = [1, 2, 3, 4]

# 第一次循环：a是下标为0的元素的值 b是下标为1的元素的值;
# 接下来每次循环：a是上次返回值的值 b是下标为2,,3,4,5...的元素的值;
# 最终reduce会将最后一次循环得到的a的值作为函数的返回值
reduce(lambda a, b: a + b, L)
