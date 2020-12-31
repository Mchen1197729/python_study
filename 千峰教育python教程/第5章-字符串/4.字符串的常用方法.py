# python中字符串的常用方法
# S.startswith(sub) 判断字符串是否以指定子串开头
# S.endswith(sub) 判断字符串是否以指定子串开头
# S.count(sub) 返回子串在字符串中出现的次数
# S.isalpha() 判断字符串是否是纯字母
# S.isdigit() 判断字符串是否是纯数字
# S.isalnum() 判断字符串是否是数字加上字母组成
# S.replace(sub) 返回被指定子串替换后的字符串

word = 'Hello World'
print(word.startswith('H'))
print(word.endswith('d'))

print(word.count('o'))
print(word.count('L'))

print(word.isalpha())
print('123'.isdigit())
print('123.456'.isdigit())
print('hello120'.isalnum())
print(word.replace('o', '0'))
print(word.replace('oo', '00'))
