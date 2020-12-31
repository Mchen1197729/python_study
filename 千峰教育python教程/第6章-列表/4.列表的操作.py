names = ['zhangsan', 'lisi', 'wangwu']

# 列表的排序
names.sort()
print(names)

# 列表的翻转
names.reverse()
print(names)

names1 = names[::-1]
print(names1)

# 列表的复制
names2 = names.copy()
print(names2, id(names2))

names3 = names[::]
print(names3, id(names3))
