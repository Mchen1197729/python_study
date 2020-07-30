# set结构：跟dict结构类似 只存储key不存储value key不可重复
# 和其他语言中的set结构不同 python中的set结构规定存储的key必须是不可变的值：数值&字符串&tuple
# 创建一个空的set结构 需要使用set() 不能使用{} 因为{}会被python解释器解释为空的dict
# 获取set结构中元素的个数 可以使用内置的len()函数
# set结构就可以理解成数学中`集合`的概念 可以进行交集&并集&差集等计算

s1 = {(1, 2, 3), (1, 2, 3), (3, 2, 1)}
print(s1, len(s1))

# 向set结构中添加元素
s1.add(100)
s1.add(100)
s1.add(100)
print(s1)

# 从set结构中删除指定的元素
s1.remove((1, 2, 3))
print(s1)

# set之间做并集&交集运算
s2 = {1, 2, 3, 4}
s3 = {2, 4, 6, 7, 9}
print(s2 & s3)  # 交集
print(s2 | s3)  # 并集
print(s2.intersection(s3))  # 交集
print(s2.difference(s3))  # 差集
print(s2.union(s3))  # 并集
