# map&reduce
from functools import reduce

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

print('*************利用切片实现反转字符串**************')
word = 'abcde'
print(word[::-1])

print('***************利用切片反转列表**************')
arr = [1, 2, 3, 4, 5]
print(arr[::-1])

print('***************filter(f,list) ***************')
print(list(filter(lambda x: x % 2 == 0, list(range(11)))))

print('***************sorted()**************')
numbers = [10, -3, -6, 7, 5, 2, 8]
# 按照默认规则进行排序
print(sorted(numbers))

# 按照指定的规则进行排序
print(sorted(numbers, key=abs))

# 按照指定规则的倒序进行排列
print(sorted(numbers, key=abs, reverse=True))

print(numbers)

scores = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 按照成绩进行排序
print(sorted(scores, key=lambda item: item[1]))
print(sorted(scores, key=lambda item: item[1], reverse=True))

# 按照姓名进行排序
print(sorted(scores, key=lambda item: item[0]))
print(sorted(scores, key=lambda item: item[0], reverse=True))

print('*****************tuple和list的解构赋值********************')
x1, x2, x3 = [1, 2, 3]
x4, x5 = (4, 5)
print(x1, x2, x3, x4, x5, end=' ')

print('**************利用闭包实现计数器**************')


def createCounter():
    counter = [0]

    def count():
        counter[0] = counter[0] + 1
        return counter[0]

    return count


c = createCounter()
print(c(), c(), c(), end=' ')
