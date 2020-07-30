# Iterable对象：指那些可以通过for...in循环类遍历的数据类型
# Iterator对象：指那些不仅可以通过for...in循环还可以通过next()函数进行循环遍历的数据类型
# Iterator对象是 Iterable对象的子集

from collections.abc import Iterable, Iterator

print(isinstance({}, Iterator))
print(isinstance({}, Iterable))

# 可以通过内置函数iter()从一个Iterable对象得到对应的Iterator对象
print(isinstance(iter({}), Iterator))
