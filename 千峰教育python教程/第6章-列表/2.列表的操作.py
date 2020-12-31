names = ['Jack', 'Rose', '张三', 'Foo', '张三', 'Bar']

# list.pop([index])-->删除末尾或者指定下标处的元素
name1 = names.pop()
print(names, name1)

name2 = names.pop(0)
print(names, name2)

# list.remove(item)-->删除指定的元素(默认只删除第一个匹配的元素,如果没有找到匹配的元素会报错)
names.remove('张三')
print(names)
names.remove('张三')
print(names)
names.remove('张三')  # 报错
print(names)
