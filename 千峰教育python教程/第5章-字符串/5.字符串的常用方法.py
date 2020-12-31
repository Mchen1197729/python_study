# python中分割字符串的方法

# S.split(分隔符) 将字符串以指定分隔符进行分割,返回列表
# S.partition(分隔符) 将字符串以指定分隔符拆分为3部分,分隔符前、分隔符本身、分隔符后,返回元组
# S.rpartition(分隔符) 从右往左将字符串以指定分隔符拆分为3部分,分隔符前、分隔符本身、分隔符后,返回元组
numbers = '1-2-3-4-5-6-7-8-9'
print(numbers.split('-'))

# 利用rpartition()方法获取文件的文件名和后缀名
file = '.package.json'
file_name, separator, suffix = file.rpartition('.')
print(file_name, separator, suffix)
