# 匿名函数 lambda

# 匿名函数有个限制:就是只能有一个表达式 不用写return 返回值就是该表达式的结果
from functools import reduce

print(list(map(lambda x: x * x, [1, 2, 3])))

print(sorted([1, 2, 3, 4, 5], key=lambda x: 1 / x, reverse=True))

print(reduce(lambda x, y: x * 10 + y, [1, 2, 3, 4, 5]))

print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7])))

# 匿名函数可以赋值给变量
f = lambda x: x * x
print(f(10))


# 匿名函数可以作为返回值
def build(x, y):
    return lambda: x * x + y * y


print(build(3, 4)())
