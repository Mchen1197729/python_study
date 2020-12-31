# for-in循环:for ele in iterable:
# in后面要跟上一个可迭代对象:字符串、列表、元祖、字典、集合、range()
# range(start,end)是一个序列生成器,包左不包右

result = 0
for i in range(1, 101):
    result += i
print(result)
