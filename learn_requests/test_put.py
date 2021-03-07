import requests

if __name__ == '__main__':
    # 直接发送put请求
    # 如需要加header，auth，即参考post请求
    r = requests.put('https://httpbin.org/put', data={'hello': '北辰'})
    print(r.text)
