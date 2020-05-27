from types import MethodType


# 面向对象高级编程
class Student(object):
    def __init__(self, age):
        self.age = age


s1 = Student(23)


# 动态的给s1绑定一个方法

def set_age(self, age):
    self.age = age


def add(self, x, y):
    return x + y


s1.set_age = MethodType(set_age, s1)  # 给实例绑定一个方法
s1.add = MethodType(add, s1)
s1.set_age(27)
print(s1.age)
print(s1.add(10, 20))


# 给一个实例绑定的方法只能在该实例上访问

# 如果给一个类绑定方法 那么该类的所有实例都可以访问该方法

def class_func(self):
    print('Hello~')


Student.class_func = class_func

s1.class_func()
Student(12).class_func()

print('****************************')


# 使用__slot__来限制实例能够访问的属性(__slots__只能限制本类的属性 对派生出来的类不起作用)

class Tiger(object):
    # 表明Tiger类的实例上只有name和age属性 也不允许在类外部动态的新增其他属性
    __slots__ = ('name', 'age')

    def __init(self, name, age):
        self.name = name
        self.age = age


t1 = Tiger()
t1.name = 'King'
t1.age = 3
print(t1)
# setattr(t1, 'gender', 'Male')
