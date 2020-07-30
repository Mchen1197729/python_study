# list是python内置的数据类型 可以随时动态的添加和删除元素
# list中可以存储不同类型的数据 也可以存储相同值的元素
classmates = ['Jack', 'Rose', 'Jerry', 'Tom']

# 获取list实例的元素个数
print(len(classmates))

# 获取list实例的最后一个元素
print(classmates[-1])

# 向list实例的末尾添加元素
classmates.append('Jimmy')
print(classmates, len(classmates))

# 向list实例的指定位置插入元素
classmates.insert(1, 'Mary')  # 向索引为1的位置插入一个元素
print(classmates)

# 删除list实例末尾的元素(返回值就是被删除的那个元素)
print(classmates.pop(), classmates)

# 删除list实例指定位置的元素 pop(i)
print(classmates.pop(1), classmates)

# list实例中的元素类型可以不相同
L = ['123', 345, True, None]
print(L)

print('***********从序列中得到列表************')
# 这种方法会产生一个变量i 可能会污染环境
# squares1 = []
# for i in range(10):
#     squares1.append(i ** 2)
# print(squares1)
# print(i)

# 这种方法不会产生变量 不会污染环境 建议使用这种方法
squares2 = [x ** 2 for x in range(10) if x % 2 == 1]
# print(x) 会报错x未定义
print(squares2)

primes = []
for x in range(2, 100):
    for y in range(2, x):
        if x % y == 0:
            break
    else:
        primes.append(x)
print(primes)

print([(x1, x2) for x1 in [1, 2, 3] for x2 in ['a', 'b', 'c']])

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x for x in arr if x % 2 == 0])
print([x for x in arr if x % 2 == 1])
print([x ** 2 for x in arr])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print([[row[j] for row in matrix] for j in range(3)])
print([row[j] for row in matrix for j in range(len(row))])
print([row for row in matrix])
