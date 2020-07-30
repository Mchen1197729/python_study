# python中函数的参数有很多种：
# 1.位置参数(普通参数)
# 2.默认参数(gender='Female')
# 3.可变参数(*args)
# 4.关键字参数(**kw)
# 5.命名关键字参数(*,hobby,married)

# 默认参数
# 默认参数最好放在参数列表的末尾 而且默认参数的值一定要设置成不可变对象：数值、字符串、tuple、None
import functools


def square(x, n=2):
    s = 1
    if n == 2:
        s = x ** 2
    else:
        while n > 0:
            n = n - 1
            s = s * x
    return s


print(square(3), square(3, 3), square(3, 1))


# 默认参数：默认参数的值必须是不可变的值
# 如果默认参数的值是可变对象的话 那么python解释器会记住上次函数调用时产生的可变参数的值从而影响到下一次函数调用的结果
def add_end1(arr=[]):
    arr.append('end')
    return arr


print(add_end1())
print(add_end1())
print(add_end1())


# 一定要将形参的默认值设置为不可变对象
def add_end2(arr=None):
    if arr is None:
        arr = []
    arr.append('end')
    return arr


print(add_end2(), add_end2())


# 函数的可变参数 args在函数内部被解释为tuple类型的数据
def display_list(*args):
    print(args)


display_list(1, 2, 3, 4)
# 简写形式
display_list(*(1, 2, 3))


# 函数的关键字参数 kw在函数内部被解释为dict类型的对象
def display_person(name, age, **kw):
    print(name, age, kw)


per = {
    'gender': 'female',
    'married': True
}
display_person('Jack', 20, gender='male', hobby=[1, 2, 3])
# 简写形式
display_person('Jack', 20, **per)


# 命名关键字参数：*号后面的参数为命名关键字参数 必须要传递指定名称的key-value键值对作为函数的参数(不能省略)
def display_named_per(name, age, *, gender, married):
    print(name, age, gender, married)


# 调用该函数的话 就只能传入含有gender和married的key-value键值对了
display_named_per('Jack', 20, **per)
display_named_per('Jack', 20, **per)

print('*******************************')


def product(*args):
    if len(args) == 0:
        return 0
    else:
        s = 1
        for i in args:
            s = s * i
        return s


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

print('****************命名关键字参数与偏函数****************')


def display(*, step=1):
    print(list(range(0, 51, step)))


display()
display10 = functools.partial(display, step=10)
display10(step=20)
