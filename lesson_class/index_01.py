class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender != 'female' and gender != 'male':
            raise ValueError('传入的性别不合法')
        else:
            self.__gender = gender


stu1 = Student('Jerry', 22)
print(stu1)
print(stu1.get_age())
