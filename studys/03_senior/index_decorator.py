# python自身就支持装饰器的语法
# 装饰器(decorator)就是用来增强函数的功能的 而且不会对函数的定义做出破坏
# 本质上 装饰器就是接受函数作为参数并且返回一个新的函数的高阶函数

# 函数对象有一个__name__属性 可以得到函数的名称
import functools


def hello():
    print('hello')


print(hello.__name__)  # hello

# 如果将函数对象赋值给其他的变量 那么该变量的__name__属性还是被赋值的函数的名称
f1 = hello

print(f1.__name__)  # hello

print('****************不接受参数的装饰器函数*******************')


# 装饰器也是一个函数 接受一个函数作为参数 并且在内部定义一个函数作为返回值
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('%s function called' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


# 相当于执行了hi = log(hi)
@log
def hi():
    print('Hi World')


hi()
print(hi.__name__)

print('********************接受参数的装饰器函数**********************')


# 如果装饰器函数需要传入参数 那么需要先编写返回装饰器函数的高阶函数

def logWithText(text):  # logWithText函数只是一个返回装饰器函数的高阶函数
    def decorator(func):  # decorator函数才是真正起作用的装饰器函数
        @functools.wraps(func)  # @functools.wrap(func) 用来保留func函数的签名 防止有些依赖函数签名的函数无法正常工作
        def wrapper(*args, **kwargs):  # wrapper函数才是最终真正被执行的函数
            print('%s function called with %s' % (func.__name__, text))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logWithText('Hello World')
def sayHi():
    print('I am sayHi')


sayHi()
print(sayHi.__name__)
