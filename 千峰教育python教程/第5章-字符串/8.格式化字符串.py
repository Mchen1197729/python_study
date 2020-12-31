# 在python中格式化字符串

# %s 字符串的占位符
print('我的名字是%s' % '刘德华')

# %d 整数的占位符
print('我今年%d岁了' % 60)

# %nd 保留n位整数 不够的用空格在前面补齐
print('我今年%5d岁了' % 60)

# %-nd 保留n位整数 不够的用空格在后面补齐
print('我今年%-5d岁了' % 60)

# %0nd 保留n位整数 不够的用0在前面补齐
print('我的名字是%s，我是%03d号男嘉宾' % ('刘德华', 7))

# %f 浮点数的占位符
print('我的体重是%f公斤' % 61.5000)

# %.nf 浮点数保留小数点后n位(四舍五入)
print('我的体重是%.2f公斤' % 61.5)
