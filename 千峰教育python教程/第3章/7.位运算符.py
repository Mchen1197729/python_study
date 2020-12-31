# python中的位运算符
# 1.& -->按位与
# 2.| -->按位或
# 3.~ -->按位亦或
# 4.^ -->按位取反
# 5.<    左移
# 6.>    右移

# 十六进制的颜色值
color = 0xF0384E
# 十六进制向右移16位得到0xF0
red = color >> 16
print(hex(red))

# 先向右移8位 然后按位与0xFF
green = color >> 8 & 0xFF
print(hex(green))

# 直接按位与0xFF
blue = color & 0xFF
print(hex(blue))

print('rgb(%s,%s,%s)' % (int(red), int(green), int(blue)))
