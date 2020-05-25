# python中的迭代

person = {
    "name": 'Tom',
    "age": 26,
    "sex": 'male',
    "married": True
}

for key in person:
    print(key)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, '===', value)

# 字符串也是可以迭代的
city = 'LosAngels'
for ch in city:
    print(ch)

# 通过collections模块的Iterable类型判断一个变量是否是可迭代的
# isinstance('abc', Iterable)  # str是否可迭代
# print(isinstance(1234, Iterable))  # int是否可迭代
# print(isinstance(['abc', 'bcd', 'cde'], Iterable))  # list是否可迭代

arr = ['吃饭', '睡觉', '打豆豆', '钓鱼']
for i, value in enumerate(arr):
    print(i, '===', value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, '===', y)

# 使用迭代查找一个list中最小和最大值，并返回一个tuple
numbers = [1, 2, 3, 4, 5, 6, 78, 99, 23, 45, 213]


def find(numbers):
    min_number = 0
    max_number = 0
    for num in numbers:
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num
    return min_number, max_number


print(find(numbers))
