import os

print(os.name)
print(os.environ.get('path').split(';'))

print(os.path.abspath('.'))

# 拼接路径
print(os.path.join('AAA', 'BB'))

# 拆分路径
print(os.path.split('AAA/BBB/CCC/file.txt'))

# 直接得到文件的扩展名
print(os.path.splitext('AAA/BBB/CCC/file.json'))

# 对文件进行重命名(要求源文件是真实存在的 否则报错)
# os.rename('student.json', 'student.py')

# 删除文件(要求文件是真实存在的 否则报错)
# os.remove('student.json')

# 得到当前文件夹下所有的目录
print(list(x for x in os.listdir('.') if os.path.isdir(x)))
# 得到当前问价夹下所有非目录文件
print(list(x for x in os.listdir('.') if not os.path.isdir(x)))
# 得到当前文件夹下所有的.py文件
print(list(x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py'))

# 列出当前目录下的所有文件(不遍历子目录)
print(os.listdir('.'))

print('**********************')


def list_dir(dir_path):
    for x in os.listdir(dir_path):
        if os.path.isdir(x):
            list_dir(x)
        else:
            print(os.path.join(dir_path, x))


list_dir('.')
