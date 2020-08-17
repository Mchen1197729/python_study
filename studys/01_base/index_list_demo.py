L1 = [1, 3, 5, 7, 9]

for i in L1[:]:
    L1.insert(0, i - 1)

print(L1)

L2 = [1, 3, 5, 7, 9]
for i, v in enumerate(L2[:]):
    L2.insert(i + i, v - 1)

print(L2)
