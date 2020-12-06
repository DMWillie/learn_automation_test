"""
    首先我们在example.py中定义了一个sum求和函数
    现在，我们加了需求，需要记录这个函数开始的时间和结束的时间
    不使用装饰器的做法如下
"""

import time

def sum(*kwargs):
    print("function start at {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
    total = 0
    for ele in kwargs:
        total += ele
    print("function end at {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
    return total

"""
后来，我们发现这个记录函数开始和结束时间的功能很好用，我们要求把这个功能加到每一个运行函数中去。
那么怎么办呢？难道要每一个函数都去加这样的代码吗?显然不太现实，这肯定不是好的做法
"""

if __name__ == '__main__':
    print(sum(1,2,3,4,5,6,7))