#  列表
squares = [1, 4, 9, 16, 25]

#  列表也是可以被切片和索引的
print(squares[0:])  # 相当于是赋值了一份原来的值
print(squares[0:2])

#  列表也支持使用 + 进行连接操作
#  注意：使用+进行连接操作原来的列表并没有发生改变 只是返回了一个新的列表
#  而list实例.append(val) 改变了原来的list实例 并且返回值是None
print('+++', squares + [36, 49, 64, 81, 100])
squares.append([36, 49, 64, 81, 100])
print('---', squares)

#  可以使用append进行添加
squares.append(999)
squares.append(888)
print(squares)

#  字符串是不可变的 但是列表是可变的 可以通过下标进行修改
squares[2] = 1000
print(squares)

#  可以对切片进行赋值 这样就可以实现对列表的修改
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = [1, 2, 3]
print(letters)
letters[:] = []  # 置空列表
print(letters)

# 用内置函数len()来获取列表的长度
print(len(squares), len(letters))

print('*********************')
# 列表是可以进行嵌套的
nested_list = [
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10]
]
print(nested_list)
print(nested_list[0][1])

print('*********************')
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b
