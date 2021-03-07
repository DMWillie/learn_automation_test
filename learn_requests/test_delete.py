import requests

if __name__ == '__main__':
    # 直接发送delete请求
    r = requests.delete('https://httpbin.org/anything', data={'hello': '北辰'})
    print(r.text)
