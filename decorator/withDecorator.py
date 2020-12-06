"""
    首先我们在example.py中定义了一个sum求和函数
    现在，我们加了需求，需要记录这个函数开始的时间和结束的时间
    使用装饰器的做法如下
"""

import time
from decorator.example import sum

"""
把计算的函数sum的函数单独抽取出来不变，把时间处理的语句另行定义函数处理。于是NoDecorator.py中的函数，
就变成了以下的样子
"""
def record_time(*kwargs):
    print("function start at {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
    total = sum(*kwargs)
    print("function end at {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
    return total

"""
以后我们再给函数加有关时间处理的功能，加到 record_time 里好了，而 sum 函数根本不用变。
那这个函数还能更加简化吗？
结合我们刚刚讲过的闭包概念，我们用外函数和内函数来替换下：
record_time就相当于我刚刚讲的outer函数，wrapper函数就是inner函数，
只不过我们的inner函数的入参是个函数，这样我们就实现了对函数本身功能的装饰。
"""
def record_time_v2(func):
    def wrapper(*kwargs):
        print("function start at {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        total = func(*kwargs)
        print("function end at {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        return total
    return wrapper



if __name__ == '__main__':
    print(sum(123,222,321))
    record_time(123,222,321)
    # 外函数，内函数，和功能函数一起，实现了不改变功能函数的前提下，给功能函数加功能的操作
    print(record_time_v2(sum)(123,222,321))

'''
假设我们的需求又变化啦，我们现在不统计函数的运行开始和结束时间了，改成统计函数的运行时长了，
那么我们只需要改 record_time_v2 这个函数就好了，而我们的功能函数 sum 就无须再改了，这样是不是方便了很多？
有了装饰器，我们可以在不改变原有函数代码的前提下，增加、改变原有函数的功能。这种方式也被称作“切面编程”，
实际上，装饰器正是切面编程的最佳释例
'''
