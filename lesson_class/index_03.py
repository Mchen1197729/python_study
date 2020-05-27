# 获取对象的类型
print(type(11))  # <class 'int'>
print(type('abc'))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({'name': 'Jack'}))  # <class 'dict'>
print(type(object))  # <class 'type'>
print(type(type(abs)))  # <class 'type'>

print(type(111) == "<class 'int'>")  # False
print(type(111) == int)  # True
print(type('111') == str)  # True
print(type([1, 2, 3]) == list)  # True
print(type((1, 2, 3)) == tuple)  # True
print(type({'name': 'Jack'}) == dict)  # True

# 如果一个变量是函数类型 也乐意用type()来判断
print(type(abs))
print(type(type(abs)) == type)  # True

print('**********************')
# 使用dir(变量)来查看变量的属性和方法
print(dir('ABC'))

print('**************************')


# setattr(obj,prop,value)、 getattr(obj,prop,[default_value])、 hasattr(obj,prop)
# 一般情况下 使用最多的就是 hasattr(obj,prop) 用来判断某个对象上是否有某个属性
class Dog(object):
    def __init__(self, name):
        self.name = name


d = Dog('Tom')

print(hasattr(d, 'name'))

setattr(d, 'age', 20)

print(getattr(d, 'age'))

print(hasattr(d, 'age'))

# 传入第三个参数 作为默认值 当该属性不存在的时候回自动使用该默认值(***使用该默认值作为返回值 而不是将该属性设置成了这个默认值***)
print(getattr(d, 'gender', 'Male'))
print(hasattr(d, 'gender'))
