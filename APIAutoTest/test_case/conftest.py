"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : conftest.py
 @Author   : xiuzhi233
 @Time     : 2024/3/9 14:07
 @Describe : 
 pytest的插件文件，存放自己写的本地插件
 主要创建自定义固件
"""

import pytest

from APIAutoTest.common.db import DB
from APIAutoTest.request_method.RequestMethod import RequestMethod


# 创建连接数据库的自定义固件
@pytest.fixture(scope="session")
def db_fixture():
    # 创建db对象并返回
    db = DB()
    yield db
    db.close()


# 创建RequestMethod类对象
@pytest.fixture(scope="session")
def request_fixture():
    # 创建request_method对象
    request_method = RequestMethod()
    yield request_method


# 解决中文显示问题
def pytest_collection_modifyitems(items):
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

