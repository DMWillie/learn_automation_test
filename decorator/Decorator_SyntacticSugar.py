"""
    装饰器语法糖
    在withDecorator.py中我们的调用仍然很麻烦，record_time_v2(sum)(1,2,3,4)的调用方式，
    不容易让使用者理解我们这个函数是在做什么，于是 Python 中为了让大家写起来方便，给了装饰器一个语法糖
    @decorator
    #对应我们的例子就是
    @record_time_v2
"""
import time

"""
使用语法糖后，在调用函数时，我们就无须再写这个装饰器函数了，
转而直接写我们的功能函数就可以了，于是我们的例子就变成了：
"""

def record_time(func):
    print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
    def wrapper(*kwargs):
        return func(*kwargs)
    print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
    return wrapper

#注意这一行，我们把record_time这个函数装饰到sum函数上
@record_time
def sum(*kwargs):
    total = 0
    for ele in kwargs:
        total += ele
    return total

if __name__ == '__main__':
    #注意此次无须再写record_time了，这样有利于大家把关注点放在功能函数本身
    print(sum(123,232,321))

