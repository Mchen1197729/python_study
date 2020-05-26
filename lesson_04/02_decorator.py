import functools
import time


def log(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s 开始调用' % fn.__name__)
        result = fn(*args, **kw)
        print('%s 调用结束' % fn.__name__)
        return result

    return wrapper


@log
def hello():
    print('Hello~')


hello()
print(hello.__name__)


# 定义一个接受参数的装饰器函数
def f1(name):
    def f2(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print('before~', name, fn.__name__)
            result = fn(*args, **kwargs)
            print('after~', name, fn.__name__)
            return result

        return wrapper

    return f2


@f1('lin_zhi_ling')
def say_hi(name):
    print('hello I am ', name)


say_hi('Rose')

print(say_hi.__name__)

print('********************************')


# 定义一个decorator函数 打印出函数执行的时间
def log_time(fn):
    functools.wraps(fn)

    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return result

    return wrapper


@log_time
def hi():
    for i in range(99999):
        pass


hi()
