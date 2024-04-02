"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : test_03_add_role.py
 @Author   : xiuzhi233
 @Time     : 2024/3/30 19:38
 @Describe : 
 
 
"""
import os
import time
import unittest
from parameterized import parameterized
from WebAutoTest.common.ReadExcel import ReadExcel
from WebAutoTest.common.ReadIni import ReadIni
from WebAutoTest.common.db import DB
from WebAutoTest.common.log import ry_log
from WebAutoTest.page.manage.add_role import RoleManage

# 获取测试的数据
datas = ReadExcel().get_data()[31:45]
read_ini = ReadIni()
# 获取日志文件的路径
log_dir = read_ini.get_report_path("LOG")
log_name = 'add_role.log'
# 获取日志对象
loger = ry_log(os.path.join(log_dir, log_name))


class TestAddRole(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """创建登录的对象"""
        cls.user_add_obj = RoleManage()
        # 创建db对象执行sql语句
        cls.db = DB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()

    @parameterized.expand(datas)
    def test_add_role(self, case_number, module_name, feature_name, case_title, case_level, case_data, case_expect,
                      sql_type, sql_sentence, update_key):
        if module_name == '角色管理' and feature_name == '添加角色':
            if sql_sentence:
                self.db.delete(sql_sentence)
            page = self.user_add_obj.add_role(roleName=case_data[0], roleKey=case_data[1], roleSort=case_data[2], status=case_data[3], menuIds=case_data[4], remark=case_data[5])
            time.sleep(1)
            # 截图
            image = case_number + ".png"
            self.user_add_obj.driver.get_screenshot_as_file(
                os.path.join(read_ini.get_report_path("IMAGES"), image))

            # 断言
            try:
                self.assertIn(case_expect, page)
            except AttributeError:
                loger.error(f"断言失败，用例编号：{str(case_number)}，期望数据：{case_expect}，实际返回数据：{page}")
                raise AttributeError("断言失败！")


if __name__ == '__main__':
    unittest.main()
