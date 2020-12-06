import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = 'https://httpbin.org/anything'
    headers = {'user-agent': 'my-app/  0.0.1'}
    payloads = {'iTesting': 'better to follow'}
    auth = {"username":"iTesting", "password": "Kevin"}
    # 直接post
    r = requests.post(url, data=payloads)
    # post带header
    r = requests.post(url, headers=headers, data=payloads)
    # post带鉴权, auth类型跟get请求支持的auth类型相同。
    r = requests.post(url, headers=headers, data=payloads,auth=HTTPBasicAuth('user', 'password'))
