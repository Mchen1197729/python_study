# 类属性vs实例属性

# 实例属性属于实例变量所有 各个实例变量之间互不干扰
# 类属性属于类所有 所有的实例变量共享同一个类属性(相当于是静态变量)
class Student(object):
    # 此处的name属于类属性
    name = 'Student'

    def __init__(self, name):
        # 此处的name属于实例属性
        self.name = name


s = Student('Jack')
print(s.name)
print(Student.name)

# 删除实例上的属性
del s.name
print(s.name)

s.name = '林志玲'
print(s.name)
print(Student.name)

del Student.name
print(Student.name)

print('***************************')


class Teacher(object):
    count = 0

    def __init__(self):
        Teacher.count += 1


t1 = Teacher()
t2 = Teacher()
t3 = Teacher()
t4 = Teacher()
print(Teacher.count)

t1.add = lambda x, y: x + y
print(t1.add(10, 20))
# print(t2.add(10, 20)) 报错
