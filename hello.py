print('hello python')

print(2 + 190)

students = ['Tom', 'Jerry', 'Rose', 'Jack']

print(len(students))

print(students)

flag = True

if flag:
    print('flag is True')
else:
    print('flag is False')

names = ('Jack', 'Rose')

print(names)

print(len(names))

tree = set([1, 2, 3, 4, 3, 2, 2, 3, 5])
print(tree)

per = {
    'name': '林志玲',
    'age': 29,
    'married': True
}

print(per.get('name'))
print(len(per))


# loop
# 1.while-loop
i = 0
while i < 100:
    i = i + 1
    print(i)

# 2.for-in
fruits = ['Apple', 'Banana', 'Peach']
for fruit in fruits:
    print(fruit)

for x in range(9):
    print(x)  # 0-8

j = 0
while j < 100:
    j += 1
    if j % 2 == 0:
        break
    print(j)
