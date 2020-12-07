import random

classmates = ['Jack', 'Rose', 'Jerry']
print(classmates)

# list.insert(index,value) 将新的值插入指定的位置
classmates.insert(1, 'Jerry')
print(classmates)

# list.append(value) 末尾添加元素
classmates.append('Tom')
print(classmates)

# list.pop() 删除末尾元素  list.pop(index) 删除指定位置的元素
classmates.pop()
print(classmates)

# list.reverse() 反转自身
classmates.reverse()
print(classmates)

# list.count(value) 返回指定的value在list中出现的次数
count = classmates.count('Jerry')
print(count)

# list.copy() 返回自身的拷贝
classmates_copy = classmates.copy()
print(classmates_copy == classmates)

# list.index(value) 返回指定的value在list中的下标
index_of_Jerry = classmates.index('Jerry')
print(index_of_Jerry)

# list.sort() 排序
classmates.sort()
print(classmates)

# list.clear() 清空自身
classmates.clear()
print(classmates)

print(random.choice(['你好']))
