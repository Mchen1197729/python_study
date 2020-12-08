# age = input('请输入您的年龄：')
# print('您明年的年纪是：', int(age) + 1)


# 把字符串转换成整数
x = '1a2c'
print(int(x, base=16))  # 将x当做十六进制的数来转换,结果是十进制

y = '0b010101'
print(int(y, base=2))  # 将y当做二进制的数来转换,结果是十进制的数字

m = '0xff00'
m1 = int(m, base=16)
print(m1)
m2 = bin(m1)
print(m2)

print(float('12.34'))

print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
print(bool(''))
print(bool(0))
