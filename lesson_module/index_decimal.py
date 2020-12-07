from decimal import *

# decimal模块中的Decimal类 用于高精度的浮点数的计算
r1 = Decimal('0.1') + Decimal('0.2')
print(r1, 0.1 + 0.2)  # 0.3 0.300000000000000000004

# 计算一件原价499元的商品按照8.9折进行销售的价格
sold_price = Decimal('499') * Decimal('0.89')
print('售价是：%s元' % sold_price)

print(Decimal('0.9') / Decimal('0.4'))  # 2.25
print(Decimal(1) / Decimal(7))
# getcontext().prec 用来设置精确度 小数点后保留几位小数
getcontext().prec = 10
print(Decimal('1') / Decimal('7'))
print(Decimal('14') / Decimal('7'))
print(getcontext().prec)
