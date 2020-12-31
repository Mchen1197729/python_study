# for-else循环:for循环中如果一直没有进入break分支,那么最终就会进入else分支.

for i in range(2, 101):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i, '是质数')
