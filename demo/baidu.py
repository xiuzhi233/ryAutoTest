"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : baidu.py
 @Author   : xiuzhi233
 @Time     : 2024/3/12 15:30
 @Describe : 
 
 
"""
# 导入 requests 包
import requests

kw = {
    "pageNum": 1,
    "pageSize": 10,
    "userName": "xiuzhi233"
}

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://47.113.217.131:88/prod-api/system/user/list", params=kw)

# 查看响应状态码
print(response.status_code)

# 查看响应头部字符编码
# print(response.encoding)

# 查看完整url地址
print(response.url)

# 查看响应内容，response.text 返回的是Unicode格式的数据
# print(response.text)
