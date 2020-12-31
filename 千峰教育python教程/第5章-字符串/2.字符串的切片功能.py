# python中字符串的切片功能很强大、很灵活
# [start:end:step] step默认为1,,不可以为0,可以为负数,返回的结果包左不包右(包含开始下标,不包含结束下标)
word = '1234567890'
m1 = word[1:5]
print(m1)  # '2345'
m2 = word[1:5:2]
print(m2)
m3 = word[5:1:-1]
print(m3)
m4 = word[-5:-3]
print(m4)
