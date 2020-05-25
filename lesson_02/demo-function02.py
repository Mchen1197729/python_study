#  函数的默认参数


def power(x, n=2):
    s = 1
    while n >= 1:
        n = n - 1
        s = s * x
    return s


print(power(2))
print(power(2, 2))
print(power(2, 3))
print(power(2, 4))

print('****************')


#  此时默认参数指向了可变对象 会造成该对象在内存中存留 可能会对下一次使用了默认参数的函数的结果产生影响
#  ***默认参数必须执行不可变对象***

def add_end(li=[]):
    print(len(li))
    li.append('END')
    return li


print(add_end(['Jack', 'Rose']))
print(add_end(['Jack', 'Rose']))
print(add_end())
print(add_end())
print(add_end())


#  可以使用None来判断用户是否传入了参数
def add_end_new(li=None):
    if li is None:
        li = []
    li.append('END')
    return li


print(add_end_new())
print(add_end_new())
print(add_end_new())
print(add_end_new())


#  使用可变参数 ->1*2 + 2*2 + 3*2 +...
def calc(*numbers):
    print(numbers)
    summary = 0
    for n in numbers:
        summary = summary + n * n
    return summary


print(calc(1, 2, 3))
numbers = [2, 3, 4]
print(calc(*numbers))


#  关键字参数
def person(name, age, **other):
    #  此处的other是传入的实参的拷贝 在此处修改other不会影响到传入的参数
    other['key'] = 'value'
    print(name, age, other)


person('Tom', 23)
person('Tom', 23, height=168, city='洛杉矶')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Rose', 34, **extra)
print(extra)


#  命名关键字参数
def new_person(*, name, age):
    print(name, age)


new_person(name='林志玲', age=44)

per = {'name': '波多野结衣', 'age': 23}
new_person(**per)


#  可变参数和命名参数一起使用
def mark(name, *args, city, job):
    print({'name': name, 'args': args, 'city': city, 'job': job})


mark('Tom', *(1, 2, 3), city='东京', job='actress')
mark('Tom', 1, 2, 3, city='东京', job='actor')


#  计算多个数的乘积
def mark_new(*args):
    summary = 1
    for n in args:
        summary = summary * n
    return summary


print(mark_new(2, 5, 10))
