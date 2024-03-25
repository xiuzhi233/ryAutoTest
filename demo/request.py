"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : request.py
 @Author   : xiuzhi233
 @Time     : 2024/3/11 15:56
 @Describe : 
 
 
"""
import json

import requests

login_url = "http://192.168.109.134:81/prod-api/login"
login_data = {"username": "admin", "password": "admin123"}
ryvue_session = requests.sessions.Session()
token = ryvue_session.request(method="POST", url=login_url, json=login_data).json().get("token")
ryvue_session.headers.update({"Authorization": "Bearer " + token})
ryvue_session.headers["Content-Type"] = "application/json;charset=UTF-8"


url = "http://192.168.109.134:81/prod-api/system/user"
put_json = {"userId": 85, "userName": "2213"}
py_text = json.dumps(put_json)
res = ryvue_session.put(url=url, data=py_text)

print(res.json())
