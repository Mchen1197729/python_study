# python中表示进制的区别

# 1.二进制-->以0b开头
x1 = 0b101101101
print(x1)

# 2.八进制-->以0o开头
x2 = 0o777
print(x2)

# 3.十进制-->正常写就行
x3 = 999
print(x3)

# 4.十六进制-->以0x开头
x4 = 0x19af
print(x4)

print(23 == 0b10111)
print(23 == 0x17)
print(23 == 0o27)
