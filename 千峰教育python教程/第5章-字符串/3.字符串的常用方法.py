# python中字符串的常用方法
word = '01234567890123456789'
# len() 获取字符串的长度
print('字符串长度为:', len(word))

# S.find(sub[,start[,end]]) 返回第一个(从左向右)子串的下标(不存在的话返回-1)
print(word.find('5'))
print(word.find('5', 2, 10))

# S.rfind(sub[,start[,end]]) 返回最后一个(从右向左)子串的下标(不存在的话返回-1)
print(word.rfind('5'))
print(word.rfind('5', 2, 10))

# S.index(sub[,start[,end]]) 返回第一个(从左向右)子串的下标(不存在的话报错)
print(word.index('5'))
print(word.index('5', 2, 10))

# S.rindex(sub[,start[,end]]) 返回最后一个(从右往左)子串的下标(不存在的话报错)
print(word.rindex('5'))
print(word.rindex('5', 2, 10))
