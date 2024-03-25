"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : __init__.py
 @Author   : xiuzhi233
 @Time     : 2024/3/10 19:13
 @Describe : 
 日志
 
"""
import functools
import os

from APIAutoTest.common.log import log

# 日志文件的路径，需要先创建好日志文件
log_path = os.path.join((os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")), "APItestLOG.log")
# 获取loger
loger = log(log_path)


# 装饰器
def log_decorator(func):
    @functools.wraps(func)  # 解决被装饰函数和方法名重名的问题，它会将被装饰的函数或方法使用原来的名称
    def inner(*args, **kwargs):
        # 在执行func之前需要获取func的名称和功能，并写入到日志
        loger.info("功能的名称为："+str(func.__name__)+" 功能的描述为："+str(func.__doc__))
        try:
            # 执行func
            result = func(*args, **kwargs)
        except Exception as e:
            # 如果有错误，需要写入到日志
            loger.error(str(e))
            # 将错误，原路返回
            raise e
        else:
            return result
    return inner