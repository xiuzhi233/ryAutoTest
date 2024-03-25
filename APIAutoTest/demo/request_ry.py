"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : request_ry.py
 @Author   : xiuzhi233
 @Time     : 2024/3/7 17:08
 @Describe : 
 
 
"""

from APIAutoTest.request_method.RequestMethod import RequestMethod

url = 'http://192.168.109.134:81/prod-api/system/user/importData?updateSupport=0'
method = "post"
mime = "application/x-www-form-urlencoded"
file = {'file1': open(r'.\user_template.xlsx', 'rb')}
req_method = RequestMethod()
response = req_method.request_all(req_url=url, case_data=None, req_method=method, req_mime=mime)
# print(response.json())
# print(response.url)
print(response.json())
