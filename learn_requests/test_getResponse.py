# -*- coding: utf-8 -*-

import requests

if __name__ == "__main__":
    s = requests.session()
    r = s.post('https://httpbin.org/anything', data={'hello': '北辰'})
    # 返回文本型response
    print("---------------1---------------------")
    print(r.text)
    # 返回文本型response，并用utf-8格式编码
    # 当你用r.text得出的结果是不可读的内容例如包括类似xu'\xe1'或者有错误提示“'ascii' codec can't encode characters in position”时，可以用encode
    print("---------------2---------------------")
    print(r.text.encode('utf-8'))
    # 获取二进制返回值
    print("---------------3---------------------")
    print(r.content)
    # 获取请求返回码
    print("---------------4---------------------")
    print(r.status_code)
    # 获取response的headers
    print("---------------5---------------------")
    print(r.headers)
    # 获取请求返回的cookies
    s.get('http://google.com')
    print("---------------6---------------------")
    print(s.cookies.get_dict())
