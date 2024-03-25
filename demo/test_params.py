"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : test_params.py
 @Author   : xiuzhi233
 @Time     : 2024/3/10 15:02
 @Describe : 
 
 
"""

import pytest
from selenium import webdriver


def setup_function():
    print("setup_function")


@pytest.fixture(params=[1, 2, 3])
def my_fixture_10(request):  # 形参的命名必须是request
    yield request.param  # request.param表示取参数化传入的每条数据


def test_10(my_fixture_10):
    assert my_fixture_10 == 2


if __name__ == '__main__':
    pytest.main()