# 将函数作为返回值

# 定义一个求和的函数 参数个数不定

def calc_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(calc_sum(1, 2, 3, 4, 5))


# 将真正进行求值的函数作为返回值
def lazy_sum(*args):
    def ca_sum():
        total = 0
        for i in args:
            total += i
        return total

    return ca_sum


print(lazy_sum(1, 2, 3)())

print('**********************')


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

print('**********利用闭包返回一个计数器函数，每次调用它返回递增整数************')


def create_counter():
    f = []

    def counter():
        f.append(0)
        return len(f)

    return counter


def counter_add():
    L1 = [0]

    def count_num():
        L1[0] += 1
        return L1[0]

    return count_num


g = counter_add()
print(g())
print(g())
print(g())
print(g())
