# 虽然通过列表生成式可以轻松的得到一个列表 但是列表存储的是真正的值
# 但是如果该列表中有大量的数据 但是真正使用到的只是几个元素 那么会造成大量的内存的浪费
# 而生成器存储的只是一种计算方法 就算存储大量的值 也不会占用很多的内存
# 生成器generator的优点：可以一边循环一边计算(类似于懒加载)

# 生成列表
print([x for x in range(10)])

# 生成generator
print((x for x in range(10)))

# generator也是可迭代对象
for i in (x for x in range(10)):
    print(i, end='-->')

print('***************使用函数来定义generator***************')


def fib(m):
    a, b, n = 0, 1, 0
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for i in fib(10):
    print(i, end=' ')

print('*****************************')


def odd():
    yield 1
    yield 3
    yield 5


for i in odd():
    print(i, end=' ')

print('***************杨辉三角****************')


def triangles(n):
    pass
