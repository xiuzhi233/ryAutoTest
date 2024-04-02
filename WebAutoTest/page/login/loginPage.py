"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : loginPage.py
 @Author   : xiuzhi233
 @Time     : 2024/3/16 22:56
 @Describe : 
 
 
"""
import os.path
import time

from WebAutoTest.basic.basic import Basic
from WebAutoTest.common.read_yaml import read_yaml
from WebAutoTest.common.ReadIni import ReadIni


class LoginPage(Basic):

    # 类属性
    yaml_data = read_yaml(ReadIni().get_file_path("LOCATOR_YAML"))

    def __init__(self, browse_name="Chrome"):
        super().__init__(browse_name="Chrome")

    def login(self, username, password):
        # 1.输入用户名
        self.send_keys(self.yaml_data["login"]["loginPage"]["username"], username)
        # 2.输入密码
        self.send_keys(self.yaml_data["login"]["loginPage"]["password"], password)
        # 3.点击登录
        self.click(self.yaml_data["login"]["loginPage"]["login_button"])
        time.sleep(0.5)

    def quit(self):
        if self.driver.current_url == "http://47.113.217.131:88/index":
            # 4.点击角标
            self.click(self.yaml_data["login"]["loginPage"]["corner"])
            # 5.点击退出登录
            self.click(self.yaml_data["login"]["loginPage"]["quit_button"])
            # 6.点击确定退出
            self.click(self.yaml_data["login"]["loginPage"]["confirm"])
        else:
            self.driver.refresh()
        return self.driver.current_url


if __name__ == '__main__':
    login = LoginPage()
    for i in range(3):
        login.login("admin", f"admin12{i + 1}")
