# generator:一边循环一边计算
g = (x * x for x in range(1, 11))
print(g)


# for i in g:
#     print(i)


# 0,1,1,2,3,5,8,13,21,34,......
def fib(n):
    i, a, b = 0, 0, 1
    while n > i:
        yield b
        a, b = b, a + b
        i += 1
    return 'done'


print(fib(6))
for f in fib(6):
    print(f)

# 下面两种写法的区别
x1, y1 = 0, 1
x1 = y1
y1 = x1 + y1
print(x1, y1)  # 1,2

x2, y2 = 0, 1
x2, y2 = y2, x2 + y2
print(x2, y2)  # 1,1


def odd():
    print('Step1')
    yield 1
    print('Step2')
    yield 3
    print('Step3')
    yield 5


for o in odd():
    pass

# 获取generator中的返回值
g = fib(6)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def triangles(n):
    print([])
