"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : log.py
 @Author   : xiuzhi233
 @Time     : 2024/3/23 21:24
 @Describe : 
 
 
"""
import logging


def ry_log(filepath):
    # 创建Logger对象
    logger = logging.getLogger()
    # 创建日志的文件handler
    handler = logging.FileHandler(filepath, mode='a', encoding="utf-8")
    # 设置日志在文件中的格式
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s - %(name)s')
    # 将格式添加到日志文件handler中
    handler.setFormatter(formatter)
    # 将日志文件handler添加到logger对象中
    logger.addHandler(handler)
    # 返回logger对象
    return logger
