import sys


# sys.argv返回一个list对象 第一个元素始终是被执行的文件名称 接下来依次是执行该文件时传入的参数
# eg:python index.py ->
#           sys.argv =>['F:/python/studys/04_module/index.py']
# eg:python index.py arg1 arg2 arg3 ->
#           sys.argv =>['F:/python/studys/04_module/index.py','arg1','arg2','arg3']

def test():
    args = sys.argv
    if len(args) == 1:
        print(args[0])
    elif len(args) == 2:
        print(args[0], args[1])
    else:
        print('Too many args')
    print(__file__)


# 如果一个.py文件是被python命令执行的话 那么python解释器会向该文件添加一个__name__的变量 值为__main__
# 但是如果一个.py文件是被当做一个模块引入的话 那么python解释器是不会讲该文件内部的__name__变量设置为__main__的
if __name__ == '__main__':
    test()
