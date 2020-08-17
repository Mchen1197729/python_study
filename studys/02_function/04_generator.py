# 定义generator函数的方式
# 1.在函数内部使用yield关键字
# 2.g = (x**2 for x in range(10))

def f1():
    yield 'first yield'
    yield 'second yield'
    yield 'third yield'


gen = f1()
print(gen)  # <generator object f1 at 0x00000216BCD42A50>

for n in gen:
    print(n)

print('*********************')
g = (x ** 2 for x in range(10))
print(g)  # <generator object <genexpr> at 0x000002656F772A50>
for m in g:
    print(m)

print('*******************')


def g1():
    a = yield 100
    print(a)
    b = yield 200
    print(b)


gg = g1()
# print(next(gg))
# print(next(gg))
print(gg.send(None))
print(gg.send(None))
