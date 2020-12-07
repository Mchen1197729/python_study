import random

# 0.取[0,1]之间随机数(double类型)
r0 = random.random()
print(r0)

# 1.在一组列表中取一个随机值
r1 = random.choice([1, 2, 3, 4, 5, 6])
print(r1)

# 2.在一组列表中取指定个数的随机值(可能会出现重复的值)
r2 = random.choices([1, 2, 3, 4, 5, 6], k=3)
print(r2)

# 3.在一组range中取指定个数的随机值
r3 = random.sample(range(0, 100), 10)
print(r3)

# 4.在一组range中取随机整数 下面的代码就是:在range(10)中取一个随机整数
r4 = random.randrange(10)
print(r4)
