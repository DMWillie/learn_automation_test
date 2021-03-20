import requests

if __name__ == '__main__':
    # 初始化一个session对象
    s = requests.Session()
    # 第一个get，先设置一个session
    # httpbin这个网站允许我们通过如下方式设置，在set后写你需要的值即可
    s.get('https://httpbin.org/cookies/set/sessioncookie/BeichenIsGood')
    # 设置好后获取所有的cookies
    r = s.get('https://httpbin.org/cookies')
    # 打印，确定我们的cookies被保存
    print(r.text)
    # 结果如下
    # '{"cookies": {"sessioncookie": "BeichenIsGood"}}'
    # 若把底8行注释掉,则结果如下
    # '{"cookies": {}}'
