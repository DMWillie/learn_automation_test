

def sum(*kwargs):
    """
    求和函数
    :param kwargs: 可变参数列表
    :return: 求和结果
    """
    total = 0
    for ele in kwargs:
        total += ele
    return total