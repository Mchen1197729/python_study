# python中字符串的常用方法
# 将字母转换成小写
print('Hello World'.lower())
# 将字母转换成大写
print('Hello World'.upper())
# 将首字母大写(只大写首字母)
print('hello world'.capitalize())
# 将每个单词的首字母大写(每个单词的首字母都大写)
print('hello world'.title())

# 确保字符串的长度,如果字符串长度超过了指定的长度则不发生任何变化,
# 如果长度不够用指定的字符补齐,ljust()左对齐,补在右边;rjust()右对齐,补在左边;center()居中对齐,补在两端
print('hello'.ljust(10, '-'))
print('hello'.rjust(10, '-'))
print('hello world123'.rjust(10, '-'))
print('apple'.center(20, '-'))

# lstrip()去除字符串左边的空格(或者指定的字符)
print('    hello'.lstrip())
# rstrip()去除字符串右边的空格(或者指定的字符)
print('hello     '.rstrip())
# strip()去除字符串两端的空格(或者指定的字符)
print('      hello     '.strip())
print('      he   llo     '.strip())

print('aaabbbaabbcccaaa'.strip('a'))

# 连接符.join(列表) 将列表转换成字符串
fruits = ['apple', 'pear', 'peach', 'banana', 'melon']
print('-'.join(fruits))

# 连接符.join(iterable[str]) 必须是字符串类型的可迭代对象(因为在python中 ·字符串+数字· 会报错)
print('*'.join('hello world'))
