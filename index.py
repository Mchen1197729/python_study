names = ('Jack', 'Rose', 'Jerry', 'Tom')
# 相当于元祖的解构赋值 其中args被python解释器解释为列表类型(就算只有一个元素或者零个元素也是被解释为列表类型)
name1, name2, name3, name4, *args = names
print(name1, name2, name3, name4, args)

print('*********************************')
per = {
    'name': 'Jack',
    'age': 29,
    'married': True
}

print(list(per.keys()))
print(sorted(per.keys()))

items = ['name', 'age', 'married']
values = ['Jack', 29, True]
print({x: x + x for x in items})

for x, y in zip(items, values):
    print('key is %s,value is %s' % (x, y))

print({x: y for x, y in zip(items, values)})

print(list(reversed(range(10))))

print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
