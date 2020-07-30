# range(start=0,end,step=1) 生成一个等差级数链表(不是列表) -> range对象:序列
# range对象占据的内存是固定的 因为它只存储start,end,step的值 而不是像list&tuple一样存储一组值
print(list(range(10)))

print(list(range(0, 10, 3)))

print(tuple(range(0, 20, 2)))

words = ['Hello', 'World', 'I', 'Love', 'You']
for i in range(len(words)):
    print(i, ':', words[i])

print(range(0, 20, 2))  # range对象 只保存start,end,step的值

# range对象是可以进行for-in遍历的
for item in range(0, 11, 2):
    print(item)

# 找出1-1000以内的所有素数
for i in range(2, 100):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end=' ')

print()


def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


fib(2000)
print()


# python中传递的形参传递的都是地址值 不管什么数据类型
def f1(li):
    li.append(10)


li = [1, 2]
f1(li)
print(li)
