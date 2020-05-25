# map(function,list)
from functools import reduce

L = [1, 2, 3]


def f(x):
    return x * x


print(list(map(f, L)))
print(list(map(str, [1, 2, 3])))


def g(x, y):
    return x + y


print(reduce(g, [1, 2, 3, 4, 5]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))

# 将字符串转换成数字
print(reduce(fn, list(map(int, '13579'))))


def str2int(string):
    def util(x, y):
        return x * 10 + y

    return reduce(util, list(map(int, string)))


print(str2int('2468091'))

print('***************************')
L1 = ['abc', 'xyz']


def fl1(x):
    return str.upper(x)


print(list(map(fl1, L1)))

print('*********************')
L2 = [1, 2, 3, 4, 5, 6, 7, 8]


def is_odd(x):
    return x % 2 == 1


print(list(filter(is_odd, L2)))
print('**************************')

L3 = [-23, -99, -54, 23, -24, 32, 1, 0, -10, 99]
print(sorted(L3))

print(sorted(L3, key=abs))

# 对字符串进行排序
L4 = ['Tom', 'Jerry', 'hello', 'world', 'apple', 'Apple', 'Rose', 'Jack']

# 按字符串默认顺序进行排序
print(sorted(L4))
# 按字符串忽略大小写进行排序
print(sorted(L4, key=str.lower))
# 按字符串忽略大小写并且进行反向排序
print(sorted(L4, key=str.lower, reverse=True))

print('************practice***************')
L5 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    # 按照名字的最后一个字母进行排序
    return t[0][-1]


# 此处的形参t就是进行排序的集合的每个元素 return的值就是进行排序的规则
def by_score(t):
    return t[1]


# 按照学生姓名进行排序
print(sorted(L5, key=by_name))

# 按照学生的成绩进行排序
print(sorted(L5, key=by_score))
