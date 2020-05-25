# Iterable Iterator
from collections.abc import Iterable, Iterator

print(isinstance('abc', Iterable))
print(isinstance('abc', Iterator))

print('**********************')
print(isinstance([], Iterable))
print(isinstance([], Iterator))

print('**********************')
print(isinstance((1, 2, 3), Iterable))
print(isinstance((1, 2, 3), Iterator))

print('**********************')
print(isinstance({'name': 'Tom'}, Iterable))
print(isinstance({'name': 'Tom'}, Iterator))

print('**********************')
print(isinstance(200, Iterable))
print(isinstance(200, Iterator))

print('**********************')
print(isinstance((x for x in range(1, 10)), Iterable))
print(isinstance((x for x in range(1, 10)), Iterator))

print('**********************')
print(isinstance(iter([]), Iterable))
print(isinstance(iter([]), Iterator))
