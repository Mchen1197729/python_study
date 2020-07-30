# python中的切片功能
# 可以用于切片操作的数据类型有：1.list 2.str 3.tuple
numbers = list(range(100))

# 取所有的数字(相当于复制了一份)
print(numbers[:])

# 取所有的数字 倒序
print(numbers[::-1])

# 取前十个数
print(numbers[0:10])

# 取最后一个数字
print(numbers[-1])

# 取最后是个数字
print(numbers[-10:])

# 取第十到第二十个数 每隔两个数取一次
print(numbers[10:20:2])

# 取所有数字 每隔5个取一次
print(numbers[::5])
