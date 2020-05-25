# Python中的装饰器:在不修改函数定义的前提下 对函数的功能进行扩展
def now():
    return '2020-05-25'


print(now())
# 函数对象有__name__属性 返回该函数对象的名称(函数定义时的函数名)
print(now.__name__)

g = lambda x: x * x
# 匿名函数的函数名返回:<lambda>
print(g.__name__)

print('***************************')


def log(func):
    def wrapper(*args, **kw):
        print('function `%s` is calling' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 相当于先执行了now = log(now)
@log
def now_time():
    return '2020-05-25'


print(now_time())

