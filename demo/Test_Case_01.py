"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : Test_Case_01.py
 @Author   : xiuzhi233
 @Time     : 2024/3/18 16:10
 @Describe : 
 
 
"""
import unittest


class Test_Case_01(unittest.TestCase):  # 新建测试类必须继承unittest.TestCase

    # 测试方法名称必须以 test 开头
    def test_01(self):
        print("测试用例名称为：test_01")

    def test_02(self):
        print("测试用例名称为：test_02")


if __name__ == '__main__':
    # 执行测试用例
    unittest.main()
