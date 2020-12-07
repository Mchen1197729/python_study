from datetime import date

now = date.today()
print(now)  # 2020-08-27
print(type(now))

birthday = date(1994, 5, 4)
today = date(2020, 8, 27)

days = today - birthday
print(days)
