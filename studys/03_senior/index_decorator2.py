import functools


# 关于装饰器函数decorator的练习
import time


def computeTime(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print('begin')
        result = fn(*args, **kwargs)
        print('end')
        return result

    return wrapper


@computeTime
def demo():
    print('demo')


demo()

print('***************写一个既可以接受参数也可以不接受参数的装饰器函数****************')


def log(fn):
    if isinstance(fn, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper1(*args, **kwargs):
                print('%s called with text: %s' % (func.__name__, fn))
                return func(*args, **kwargs)

            return wrapper1

        return decorator
    else:
        @functools.wraps(fn)
        def wrapper2(*args, **kwargs):
            print('%s called' % fn.__name__)
            return fn(*args, **kwargs)

        return wrapper2


@log('你好')
def hh():
    print('hh')


hh()

print(time.time())
