# 输入一个数字，判断改数字是否满足能够被3或者7整除，但是不能同时被3和7整除
while True:
    number = int(input('输入一个数字：'))
    if (number % 3 == 0 or number % 7 == 0) and not (number % 3 == 0 and number % 7 == 0):
        print('该数字满足要求')
    elif number == 0:
        break
    else:
        print('该数字不满足要求')
