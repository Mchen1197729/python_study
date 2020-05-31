# 使用枚举类
from enum import Enum, unique

Color = Enum('Color', ('RED', 'BLUE', 'YELLOW'))

print(Color.RED.value)

for name, member in Color.__members__.items():
    print('%s %s' % (name, member.value))

print('*************************************')


# 从Enum类派生自定义枚举类
@unique
class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


# 既可以通过枚举名称得到枚举值 也可以通过枚举值得到枚举名称
print(Direction.DOWN)
print(Direction.DOWN.value)
print(Direction(1))

print('***************************')


class Gender(Enum):
    MALE = 1
    FEMALE = 0


class Student(object):
    def __init__(self, gender):
        if not isinstance(gender, int):
            raise TypeError('传入的数据类型不合法')

        self.gender = Gender(gender)


s1 = Student(Gender.MALE.value)
print(s1.gender)

print(type(Student))
print(type(s1))

