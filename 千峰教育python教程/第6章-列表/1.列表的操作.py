names = ['Jack', 'Rose', 'Foo', 'Bar']

# list.append(元素)-->在列表末尾追加一个元素
names.append('黄飞鸿')
print(names)

# list.insert(index,元素)-->在指定下标处插入元素

names.insert(2, '胡一刀')
print(names)

# list.extend(可迭代对象)-->在列表末尾追加一个可迭代对象
names.extend(['刘德华', '郭富城'])
print(names)

m = 0
n = 1
m, n = (n, m)
print(m, n)
