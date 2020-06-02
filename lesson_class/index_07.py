# 定制类的功能
class Student(object):
    def __init__(self, name):
        self.name = name

    # 相当于toString()
    def __str__(self):
        return 'Student with name: %s' % self.name

    __repr__ = __str__

    # 能够使用for-in遍历
    def __iter__(self):
        pass


print(Student('Tom'))
Student('Jack')

print('***************************')


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        if self.a > 999:
            raise StopIteration()
        return self.a

    # 使用下标获取指定的元素 实例[item]
    def __getitem__(self, item):
        a, b = 1, 1
        for n in range(item):
            a, b = b, a + b
        return a


fib = Fib()

for i in fib:
    print(i)
print('------', Fib()[0])
print('------', Fib()[1])
print('------', Fib()[2])
print('------', Fib()[3])
print('------', Fib()[4])
print('------', Fib()[5])
print('------', Fib()[6])
print('------', Fib()[7])

print('***********************************')


class Demo(object):
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 2
        if self.number > 100:
            raise StopIteration()
        return self.number


demo = Demo()

for number in demo:
    print(number)

print('********__getattr__********')


class Dog(object):
    def __init__(self, gender):
        self.gender = gender

    def __getattr__(self, item):
        if item == 'age':
            return 18
        elif item == 'say_hi':
            return lambda: 'hello'
        elif item == 'hi':
            return lambda: print('Hi~')
        raise AttributeError('属性名不存在')


print(Dog('Male').gender)
print(Dog('Male').age)
print(Dog('Male').say_hi())
Dog('Male').hi()
# print(Dog('Male').name_name)

print('***********************************')


class Ch(object):
    def __init__(self, ch=''):
        self.ch = ch

    def __getattr__(self, ch):
        return Ch('%s/%s' % (self, ch))

    def __str__(self):
        return self.ch

    __repr__ = __str__


print(Ch('/prop').user.message)


class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__


print(Chain('/api').user.message)

print('*****************************')


class URL(object):
    def __init__(self, url=''):
        self.url = url

    def __getattr__(self, url):
        return URL('%s/%s' % (self.url, url))

    def __str__(self):
        return self.url

    __repr__ = __str__


print('*********************************')


class Snake(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('my name is %s' % self.name)


Snake('眼镜蛇')()
print(callable(Snake('abc')))
