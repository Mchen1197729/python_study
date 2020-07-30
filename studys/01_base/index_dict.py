# dict是python内置的一种数据类型 用于存放ket-value形式的元素
# dict的key必须是不可变对象 因为dict要根据key来计算出存储的位置(利用Hash算法 以便于快速查找)
# dict占用空间较大 但是查找和插入的效率高;list占用空间较小 但是查找和插入的效率略低
d1 = {
    'name': 'Jack',
    'age': 29,
    'married': True
}

print(d1)
# 获取指定key对应的value需要使用d1[key]或者d1.get(key[,defaultVal])
print(d1['name'], d1.get('gender'), d1.get('salary', 9999))

for key in d1:
    print(d1[key], '---', d1.get(key))

print('************删除dict的key************')

# 删除dict中指定的key 使用pop(key)或者del dict[key]
d1.pop('married')  # 删除d1中married属性
print(d1)

# dict的key通常是数值和字符串 因为数值和字符串都属于不可变对象
# tuple是可以作为dict的key使用的 因为tuple也属于不可变对象
# 但是list是不可以作为dict的key的 因为list是可变对象 无法计算hash
t = (1, 2)
d2 = {
    t: 'tuple_value'
}
print(d2.get(t))

print('*************使用dict.items()来遍历dict的key-value**************')
for k, v in d1.items():
    # v = v + 'Hello' 可以改变值
    print(k, '--', v)

for k in d1.keys():
    print(k)

for v in d1.values():
    print(v)

print(d1.keys(), d1.values(), d1.items())

# 对于list 如果想要同时得到索引和索引对应的值 可以使用enumerate()函数
for k, v in enumerate([1, 2, 3, 4]):
    print(k, '--', v)

print('********************************************')
todos = [
    {
        'id': 1,
        'title': '吃饭',
        'completed': True
    },
    {
        'id': 2,
        'title': '睡觉',
        'completed': True
    },
    {
        'id': 3,
        'title': '打豆豆',
        'completed': False
    }
]

print([item for item in todos if item.get('completed')])
print([item for item in todos if item.get('title') == '吃饭'])
print([item.get('id') for item in todos if item.get('completed')])
