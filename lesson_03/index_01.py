# 切片功能:用于操作list和tuple以及字符串(str)

hobbies = ['吃饭', '睡觉', '打豆豆']

print(hobbies[0:3])
print(hobbies[0:4])
print(hobbies[:2])
print(hobbies[3:5])
print(hobbies[-1])
print(hobbies[-1:])
print(hobbies[-3:-1])

numbers = list(range(100))
#  前十个数
print(numbers[:10])
#  后十个数
print(numbers[-10:])
# 前十个数 间隔为2
print(numbers[:10:2])
# 所有数 间隔为5
print(numbers[::15])

# 复制一个list
print(numbers[:])

print('********************')
numbers2 = range(10)
print(*numbers2[:])

print('********************')

name = 'Jerry'
print(name[1:])
print(name[:3])
print(name[:-1])


# 定义一个函数trim() 实现去除字符串两端的空格
def trim(string):
    while True:
        if string[0] == ' ':
            string = string[1:]
        elif string[-1] == ' ':
            string = string[:-1]
        else:
            return string


name = ' Jerry '
print(trim(name))
print(name)
