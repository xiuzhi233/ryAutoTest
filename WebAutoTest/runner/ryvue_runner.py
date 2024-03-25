"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : ryvue_runner.py
 @Author   : xiuzhi233
 @Time     : 2024/3/23 15:19
 @Describe : 
 
 
"""
import unittest
import unittestreport
from WebAutoTest.common.ReadIni import ReadIni


if __name__ == '__main__':
    # 创建测试套
    suite = unittest.TestSuite()
    # 创建loader
    loader = unittest.TestLoader()
    # 获取用例层目录
    read_ini = ReadIni()
    # for i in os.scandir(read_ini.get_case_path("TEST_CASE")):
    test_case = read_ini.get_case_path("TEST_CASE")
    # 使用loader将用例添加到测试套中
    suite.addTest(loader.discover(test_case, pattern="test*.py"))
    # 获取HTML报告的路径
    report_dir = read_ini.get_report_path("HTML")
    # HTML报告的名称
    report_name = "若依web自动化测试报告.html"
    # 创建runner
    runner = unittestreport.TestRunner(suite=suite,
                                       filename=report_name,
                                       report_dir=report_dir,
                                       title="ryvue-web自动化测试",
                                       tester="测试员-李福冉",
                                       desc="ryvue项目测试报告",
                                       templates=1
                                       )
    # 使用runner执行测试套
    runner.run()
