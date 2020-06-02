# StringIO
from io import StringIO, BytesIO

s = StringIO()
s.write('Hello')
s.write('~')
s.write('World')
# 可以通过getvalue()方法获取文件的内容
print(s.getvalue())

# 也可以通过read()方法读取文件的内容
si = StringIO('HELLO')
print(si.read())

print('****************************')
bi = BytesIO()
bi.write('中国'.encode('gbk'))
print(bi.getvalue())
