"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : RequestMethod.py
 @Author   : xiuzhi233
 @Time     : 2024/2/19 15:33
 @Describe : 
 
 
"""
import requests
from APIAutoTest.common.ReadExcel import ReadExcel


class RequestMethod:
    def __init__(self):
        """管理登录的状态"""
        # 配置登录数据
        login_data = {"username": "admin", "password": "admin123"}
        # 配置登录的url
        login_url = ReadExcel().case_url(2)
        # 创建session对象，用来请求
        self.ryvue_session = requests.sessions.Session()
        # 提取token，使用request方法获取服务器返回的数据，并将数据转成python中的json对象，字典获取token
        token = self.ryvue_session.request(method="POST", url=login_url, json=login_data).json().get("token")
        # 将token关联到session对象的headers中
        self.ryvue_session.headers.update({"Authorization": "Bearer " + token})

    # 封装公共的请求方法
    def request_all(self, req_url, req_method, req_mime=None, case_data=None):
        """
        封装公共的请求方法
        :param req_url:请求路径
        :param req_method:请求方法
        :param req_mime:请求媒体类型
        :param case_data:请求的数据
        :return:Response Type
        """

        # 判断媒体类型是否为表单类型，如果是，使用data传参
        if req_mime == "application/x-www-form-urlencoded" or req_mime == "x-www-form-urlencoded":
            return self.ryvue_session.request(method=req_method, url=req_url, data=case_data)

        # 判断媒体类型是否为json传参，如果是，使用json传参
        elif req_mime == "application/json" or req_mime == "json":
            return self.ryvue_session.request(method=req_method, url=req_url, json=case_data)

        # 判断媒体类型是否为上传文件，如果是，使用files传参
        elif req_mime == "multipart/form-data" or req_mime == "form-data":
            return self.ryvue_session.request(method=req_method, url=req_url, files=case_data)

        # 判断媒体类型是否为地址栏传参，如果是，使用params传参
        elif req_mime == "query" or req_mime == "params" or req_mime == "param":
            return self.ryvue_session.request(method=req_method, url=req_url, params=case_data)

        # 判断媒体类型是否为None，表示没有传参
        elif req_mime is None:
            return self.ryvue_session.request(method=req_method, url=req_url, data=None, json=None, params=None,
                                              files=None)

        # 判断媒体类型是否query|json，表示地址栏和请求体中同时传参，使用params和json同时传参
        elif req_mime == "query|json" or req_mime == "json|query" or req_mime == "params|json":
            return self.ryvue_session.request(method=req_method, url=req_url, params=case_data["query"],
                                              json=case_data["json"])

        # 判断媒体类型是否text或者为text/plain，表示请求体中传纯文本，使用data传参
        elif req_mime == "text" or req_mime == "text/plain":
            return self.ryvue_session.request(method=req_method, url=req_url, data=case_data)

        else:
            raise NameError("传入的媒体类型，没有封装，请自行封装!")


if __name__ == '__main__':
    req = RequestMethod()
    kw = {
        "pageNum": 1,
        "pageSize": 10,
        "userName": "xiuzhi233"
    }
    response = req.request_all(req_method="get", case_data=kw,
                               req_url="http://192.168.109.134:81/prod-api/system/user/list")
    print(response.url)
