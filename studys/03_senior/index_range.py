# python中强大的列表生成器


# 生成1-10的数字组成的数组
print([x for x in range(11)])

# 生成1-10的数字的平方组成的数组
print([x ** 2 for x in range(11)])

# 生成1-10之间所有的奇数组成的数组
print([x for x in range(11) if x % 2 == 1])

# 使用两层循环(两层循环之间互不相干)
print([x + y for x in 'abc' for y in 'XYZ'])

# 注意与上面的区别(这个只是一层循环)
print([x + y for x, y in zip('abc', 'XYZ')])

# 使用嵌套循环
nest_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print([i for item in nest_numbers for i in item])

print([[i] for item in nest_numbers for i in range(3)])

print([[i for item in nest_numbers] for i in range(3)])

print([[item[i] for item in nest_numbers] for i in range(3)])

print('**********************************')
words = ['Hello', 'World', 18, 'Apple', None]
print([str(x).lower() for x in words])

# 如果if放在for的前面 那么必须有else才能行
print([x.lower() if isinstance(x, str) else str(x).lower() for x in words])

# 如果if放在for的后面 那么不可以加else语句
print([x.lower() for x in words if isinstance(x, str)])
