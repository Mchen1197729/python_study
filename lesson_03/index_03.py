#  列表生成式 range(number)
print(range(10))

for i in range(10):
    print(i)

print(list(range(10)))

# 生成[1*1,2*2,3*3...,10*10]
L = []
for i in range(1, 11):
    L.append(i * i)
print(L)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for i in L1:
    if isinstance(i, str):
        L2.append(i.lower())
    else:
        L2.append(str(i).lower())
print(L2)

print([m + n for m in 'ABC' for n in 'XYZ'])

ss = []
for m in 'ABC':
    for n in 'XYZ':
        ss.append(m + n)
print(ss)

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([x * x if x % 2 == 0 else x * x * x for x in range(1, 11)])

print([i.lower() if isinstance(i, str) else str(i).lower() for i in L1])
print([str(x).lower() for x in L1])
