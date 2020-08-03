from datetime import datetime

# datetime模块中有一个类也叫datetime
now = datetime.now()
print(now)
print(type(now))

# 创建制定的datetime对象 datetime(年,月,日,时,分,秒)
dt = datetime(2015, 10, 8, 11, 30)
print(dt)

# 将datetime类型装换为timestamp
ts = dt.timestamp()
print(ts)

# 将timestamp转换为datetime
dt2 = datetime.fromtimestamp(ts)
print(dt2)
