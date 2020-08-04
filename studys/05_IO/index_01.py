with open('./file/hello.text', 'r') as f:
    print(f.tell())  # file.tell() 查看此时此刻的指针指向何处
    print(f.read())
    print(f.tell())
    f.seek(1)  # file.seek(num) 将指针重新指向指定的位置
    print(f.read())  # file.read() 从当前指针处一直读取到结尾处的内容

print('*********************************')

with open('./file/abc.txt', 'a') as f1:
    f1.write('abcdefg')
    print(f1.tell())
