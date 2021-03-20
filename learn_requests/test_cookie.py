# -*- coding: utf-8 -*-

import requests

if __name__ == "__main__":
    # url = 'https://gate.lagou.com/v1/entry/message/newMessageList'
    # cookie = {'cookie': '_gid=GA1.2.438589688.1601450871; gate_login_token=475844a837230240e1e73e4ecfa34102e65fa8e5384801cca67bbe983a142abb;'}
    # headers = {'x-l-req-header': '{deviceType: 9}'}
    # s = requests.Session()
    # # 直接带登录态发送请求
    # r = s.get(url, cookies=cookie, headers=headers)
    # # 不经过登录，也能访问登录后才能访问的接口
    # print(r.text)
    # {"state":1,"message":"成功","content":{"newMessageList":[],"newMessageCount":0}}

    api = "https://gate.lagou.com/v1/neirong/kaiwu/getAllCoursePurchasedRecordForPC"
    headers = {'x-l-req-header': '{deviceType: 1}'}
    cookie = {'cookie': 'LG_LOGIN_USER_ID=3c8d2942ba5f89efff5da4d0c7ae0f401bab2b81f777b4a2cc6983c18b846ec0; gate_login_token=8de613ba272bd832c7b720c964e09d151dd67f36dd859813aebee75287584661;'}
    s = requests.Session()
    re = s.get(api, cookies=cookie, headers=headers)
    print(re.text)
    # 不带header时返回: {"state": 1003,"message": "非法的访问"}
    # 不带cookie或cookie非法时返回: {"state": 1004,"message": "身份认证失败"}
    # 带合法的cookie返回:
    # {"state":1,"message":"操作成功","content":{"memberAdsBar":{"identityCode":1,"title":"超级VIP","tips":"全场专栏任意学","buttonText":"免费开通","url":"lagou://lagou.com/h5/open?hideTitle=1&url=https%3A%2F%2Fkaiwu.lagou.com%2Fmember%2Findex"},"allCoursePurchasedRecord":[{"courseType":2,"title":"专栏课程","bigCourseRecordList":null,"courseRecordList":[{"id":482,"name":"测试开发入门与实战","h5Url":"https://www.lagou.com/center/login?forward=https%3a%2f%2fkaiwu.lagou.com%2fcourse%2fcourseInfo.htm%3fcourseId%3d482%26sid%3d20-h5Url-0","lastLearnLessonName":"19 | 命令行参数，助力测试框架高度定制化","image":"https://s0.lgstatic.com/i/image/M00/5B/9E/Ciqc1F9_0miAAT-JAABNc8DxHQU469.png","openWebToStudy":null,"hasCourseWeChatGroup":false,"courseWeChatGroupTips":null,"updateProgress":"共29讲 / 已全部更新","updateTips":null,"lessonUpdateNum":0,"isEnterpriseCourse":false,"isCampusCourse":false,"vipFreeCourse":false,"classCourseType":null},{"id":377,"name":"微服务质量保障 20 讲","h5Url":"https://www.lagou.com/center/login?forward=https%3a%2f%2fkaiwu.lagou.com%2fcourse%2fcourseInfo.htm%3fcourseId%3d377%26sid%3d20-h5Url-0","lastLearnLessonName":"结束语 | QA 如何打造自身的核心竞争力？","image":"https://s0.lgstatic.com/i/image/M00/5B/A6/CgqCHl9_0BSAVZQDAABPt7DfHxM217.png","openWebToStudy":null,"hasCourseWeChatGroup":false,"courseWeChatGroupTips":null,"updateProgress":"共20讲 / 已全部更新","updateTips":null,"lessonUpdateNum":0,"isEnterpriseCourse":false,"isCampusCourse":false,"vipFreeCourse":false,"classCourseType":null},{"id":287,"name":"Go 微服务实战 38 讲","h5Url":"https://www.lagou.com/center/login?forward=https%3a%2f%2fkaiwu.lagou.com%2fcourse%2fcourseInfo.htm%3fcourseId%3d287%26sid%3d20-h5Url-0","lastLearnLessonName":"06 | Go 语言开发快速回顾：语法、数据结构和流程控制","image":"https://s0.lgstatic.com/i/image/M00/5B/A6/CgqCHl9_z7OAKI9oAABFLLEpSWs256.png","openWebToStudy":null,"hasCourseWeChatGroup":false,"courseWeChatGroupTips":null,"updateProgress":"共38讲 / 已全部更新","updateTips":"5更新","lessonUpdateNum":5,"isEnterpriseCourse":false,"isCampusCourse":false,"vipFreeCourse":false,"classCourseType":null}]}],"courseOrderSynEntry":null},"uiMessage":null}