# 字符串 & 字符编码
# 编码是为了让机器能看懂 而解码是为了让人能看懂 同时需要遵循指定的编码、解码方式(字符编码)
name = 'Jack'
language = '中文'
greeting = 'Hello,张三'
# 将字符串按照指定的字符编码进行编码 得到的是bytes
# 纯英文的字符串不管以ASCII字符编码还是以UTF-8字符编码 得到的bytes都是一样的
# 但是如果字符串中含有中文字符 那么使用ASCII字符编码的话会报错
print(name.encode('UTF-8'), name.encode('ASCII'), language.encode('UTF-8'), greeting.encode())

# 声明bytes需要在字符串前加上b符号来表示这是一个bytes
b1 = b'\xe4\xb8\xad\xe6\x96\x87'
b2 = b'Hello,\xe5\xbc\xa0\xe4\xb8\x89'
print(b1.decode('UTF-8'), b2.decode())

print('*********************')
# len()函数如果传入一个字符串 那么计算的是该字符串的字符数
print(len('中文'))
# len()函数如果传入一个bytes 那么就是计算该bytes的字节数
# 传入的参数是`中文`的bytes形式 由此可见一个中文字符通常占据3个字节数(有例外情况)
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

print('************输出格式化的字符串************')
# 占位符 %s->字符串的占位符 %d->数值的占位符 %f->浮点数的占位符
# 如果字符串中需要输出% 则需要使用两个%(%%)进行转译
username = '刘德华'
month = 10
fee = 200
balance = 999
rate = 95
print('亲爱的%s,你好,你%d月份的话费是%d元,目前的余额是%d元,恭喜你超过%d%%的用户' % (username, month, fee, balance, rate))

# 字符串的format()方法也可以实现输出格式化的字符串
print('Hello,{0},成绩提升了{1}%'.format('小花', 20.6))
