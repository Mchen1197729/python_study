# 调用函数

number1 = max(1, 2, 3, 4, 5, 7, 8, 9)
print(number1)
number2 = min(1, 2, 3, 4, 5, 7, 8, 9)
print(number2)

# 函数名就相当于一个地址的引用 可以赋值给另一个变量

print(int('12'))  # 12 (数值)
print(int(12.34))  # 12 (数值)
print(float('12.34'))  # 12.34 (数值)
print(float('12'))  # 12.0 (数值)

print(str(12.34))  # '12.,34' (字符串)

print(bool(1))  # True
print(bool(0))  # False
print(bool('1'))  # True
print(bool('0'))  # True

# hex(number) 将证书转换成16进制的字符串
print(hex(255))


# 定义函数 def

def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-100))


# 空函数 (可以理解为占位符 先让代码可以运行下去)
def f_empty():
    pass


# 求x的阶乘
def my_func(x):
    summary = 1
    while x >= 1:
        summary = summary * x
        x = x - 1
    return summary


print(my_func(1))
print(my_func(2))
print(my_func(3))
print(my_func(4))
print(my_func(5))


# 函数的参数
def f(x):
    return x * x


#  求x的n次幂
def fn(x, n):
    total = 1
    while n >= 1:
        total = total * x
        n = n - 1
    return total


print(fn(2, 1))
print(fn(2, 2))
print(fn(2, 3))
print(fn(2, 4))
print(fn(2, 5))


# 求n的阶乘
def fx(n):
    if n == 1:
        return n
    else:
        return n * fx(n - 1)


print(fx(1))
print(fx(2))
print(fx(3))
print(fx(4))
print(fx(5))


#  求x的n次幂

def f1(x, n):
    if n == 1:
        return x
    else:
        return x * f1(x, n - 1)


print(f1(2, 1))
print(f1(2, 2))
print(f1(2, 3))
print(f1(2, 4))


#  求斐波那契数
def fbnq(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fbnq(n - 1) + fbnq(n - 2)


print(fbnq(1))
print(fbnq(2))
print(fbnq(3))
print(fbnq(4))
print(fbnq(5))
print(fbnq(6))
print(fbnq(7))
print(fbnq(8))
print(fbnq(9))
print(fbnq(10))
print(fbnq(11))
print(fbnq(12))
