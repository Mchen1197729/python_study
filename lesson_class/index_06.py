# 使用@property 是一个装饰器 作用是将类中定义的方法转换为属性(getter&setter)
class Student(object):
    def get_score(self):
        return self._score

    # 对传入的score做验证
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('传入的数据不合法')
        elif score < 0 or score > 100:
            raise ValueError('成绩不在合理的范围')
        else:
            self._score = score


s1 = Student()

s1.set_score(78)
print(s1.get_score())
# s1.set_score(101)

print('**********使用@property************')


class Student1(object):
    # @property将score()方法转换成score属性(getter) 同时生成了一个名为@score.setter的装饰器(可以使用也可以不使用)
    @property
    def score(self):
        return self._score

    # 该装饰器将score(self,score)方法转变为属性(setter) 并且允许自定义验证规则
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise TypeError('传入的数据类型不合法')
        elif score > 100 or score < 0:
            raise ValueError('传入的成绩不在合法范围')
        self._score = score

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth

    @property
    def age(self):
        return 2020 - self._birth


print('****************************')


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('传入的数据类型不正确')
        elif width < 0:
            raise ValueError('传入的数值不合法')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('传入的数据类型不正确')
        elif height < 0:
            raise ValueError('传入的数值不合法')
        self._height = height

    @property
    def resolution(self):
        return self._width * self._width + self._height * self._height
