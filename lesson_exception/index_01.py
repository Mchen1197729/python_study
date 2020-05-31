import logging

try:
    r = 0
    print(10 / r)
except ZeroDivisionError as e:
    print('exception:', e)
finally:
    print('finally')
print('END')

print('**************************8')


def divide(n):
    return 10 / n


try:
    divide(0)
except Exception as e:
    print('出错了')
finally:
    print('Finally')
print('END~')
