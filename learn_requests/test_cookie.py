# -*- coding: utf-8 -*-

import requests

if __name__ == "__main__":
    url = 'https://gate.lagou.com/v1/entry/message/newMessageList'
    cookie = {'cookie': '_gid=GA1.2.438589688.1601450871; gate_login_token=475844a837230240e1e73e4ecfa34102e65fa8e5384801cca67bbe983a142abb;'}
    headers = {'x-l-req-header': '{deviceType: 9}'}
    s = requests.Session()
    # 直接带登录态发送请求
    r = s.get(url, cookies=cookie, headers=headers)
    # 不经过登录，也能访问登录后才能访问的接口
    print(r.text)
    # {"state":1,"message":"成功","content":{"newMessageList":[],"newMessageCount":0}}
    # {"state": 1004,"message": "身份认证失败"}