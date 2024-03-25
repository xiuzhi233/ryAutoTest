"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : test_01_login.py
 @Author   : xiuzhi233
 @Time     : 2024/3/17 13:45
 @Describe : 
 
 
"""
import os
import unittest
from parameterized import parameterized
from WebAutoTest.common.ReadExcel import ReadExcel
from WebAutoTest.common.ReadIni import ReadIni
from WebAutoTest.common.log import ry_log
from WebAutoTest.page.login.loginPage import LoginPage

# 获取测试的数据
datas = ReadExcel().get_data()[:12]
read_ini = ReadIni()
# 获取日志文件的路径
log_dir = read_ini.get_report_path("LOG")
log_name = "login.log"
# 获取日志对象
loger = ry_log(os.path.join(log_dir, log_name))


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """创建登录的对象"""
        cls.login_obj = LoginPage()

    @parameterized.expand(datas)
    def test_login(self, case_number, module_name, feature_name, case_title, case_level, case_data, case_expect,
                   sql_type, sql_sentence, update_key):
        if module_name == '系统认证' and feature_name == '登录系统':
            self.login_obj.login(username=case_data[0], password=case_data[1])

            # 截图
            image = case_number + ".png"
            self.login_obj.driver.get_screenshot_as_file(os.path.join(read_ini.get_report_path("IMAGES"), image))
            current_url = self.login_obj.quit()

            # 断言
            try:
                self.assertEqual(current_url, case_expect)
            except AttributeError:
                loger.error(f"断言失败，用例编号：{str(case_number)}，期望数据：{case_expect}，实际返回数据：{current_url}")
                raise AttributeError("断言失败！")


if __name__ == '__main__':
    unittest.main()
