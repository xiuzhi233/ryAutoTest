"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : log.py
 @Author   : xiuzhi233
 @Time     : 2024/3/7 14:17
 @Describe : 
 日志装饰器
 
"""

import logging


def log(filename):
    """

    :param filename:
    :return:
    """
    # 创建logger对象
    loger = logging.getLogger()

    # 创建文件的控制器，将日志写入到文件中
    handler = logging.FileHandler(filename, mode="a", encoding="utf-8")

    # 设置日志文件中的内容格式
    formatter = logging.Formatter('%(levelname)s--%(asctime)s--%(message)s')

    # 格式添加到文件的控制器中
    handler.setFormatter(formatter)

    # logger对象添加文件控制器
    loger.addHandler(handler)

    # 设置日志文件的级别
    loger.level = logging.INFO

    return loger

