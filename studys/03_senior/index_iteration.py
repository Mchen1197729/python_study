# python中对可迭代对象进行迭代操作(遍历)
numbers = range(100)
for i in numbers:
    if i % 5 == 0:
        print(i)

student = {
    'name': '林志玲',
    'age': 28,
    'gender': 'Female'
}

for key in student:
    print(key, '--', student.get(key))

for k, v in student.items():
    print(k, '--', v)

numbers2 = [1, 2, 3, 4, 5, 6]
for num in numbers2:
    print(num)

# python提供了内置函数enumerate来将list对象变成索引-值的可迭代对象
for i, v in enumerate(numbers2):
    print(i, '---', v)

# 下面是一些特殊的迭代
print('***************下面是一些特殊的迭代****************')
# tuple&list都是可以进行`解构赋值`的,但是dict对象是不可以进行`解构赋值`的
list_tuple = [(1, 2), (2, 3), (3, 4)]
for x, y in list_tuple:
    print(x, y)

list_list = [[1, 2], [2, 3], [3, 4]]
for x, y in list_list:
    print(x, y)

list_dict = [
    {'key': 0, 'value': 1},
    {'key': 1, 'value': 2},
    {'key': 2, 'value': 3},
    {'key': 3, 'value': 4}
]

for k1, v1, k2, v2 in list_dict:
    print(k1, v1, k2, v2)

