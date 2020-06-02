with open('./data/hello.txt', 'r') as f:
    print(f.read())

with open('./data/.env.development', 'r') as f2:
    for line in f2.readlines():
        print(line.strip())

# 用'rb'模式打开二进制文件
with open('./data/github.jpg', 'rb') as f2:
    print(f2.read())

# 用encoding指定字符编码
with open('./data/hello.txt', 'r', encoding='gbk') as f3:
    print(f3.read())

# 写文件 用'w'或者'wb'或者'a'表示写入文件
with open('./data/hello.txt', 'a') as w1:
    w1.write('Hello World~')

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as ff:
    s = ff.read()
    print(s)
