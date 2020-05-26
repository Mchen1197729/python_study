# Python中的继承和多态
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('Animal is running...')


# 创建Animal类的子类

class Dog(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def bark(self):
        print('Dog is barking...')

    def run(self):
        print('Dog is running...')


a = Animal('吉吉国王', 29)
d = Dog('大黄', 3, 'male')
print(isinstance(a, Animal))
print(isinstance(d, Dog))
print(isinstance(d, Animal))  # True:表明子类的对象也是父类的实例
print(isinstance(a, Dog))  # False


def run_twice(animal):
    if isinstance(animal, Animal):
        animal.run()
        animal.run()
    else:
        raise ValueError('传入的参数类型不匹配')
    # animal.bark()


run_twice(a)
run_twice(d)
run_twice(111)  # 报错
