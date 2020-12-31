# python中字符串的编码集

# char(编码)-->将指定的编码转换为对应的字符(Unicode编码集)
print(chr(97))

# ord(字符)-->将指定的字符转换为对应的编码(Unicode编码集)
print(ord('a'))

# gbk编码下一个中文字符占两个字节;utf8编码下一个中文字符占三个字节
# '字符'.encode('编码集')-->得到指定字符在指定编码集下对应的数字(十进制的数字)
print('陈'.encode('gbk'))  # 0b10110011 11000010
print('陈'.encode('utf8'))  # 0b11101001 10011001 10001001

print(type('陈'.encode('gbk')))

print(b'\xe9\x99\x88'.decode('utf8'))

