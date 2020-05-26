' a test module '

__author__ = 'Mchen1197729'

import sys


def test():
    args = sys.argv
    # sys.argv是一个list 第一个元素是python 执行的脚本名称 接下来依次是传入的参数
    print(sys.argv)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
