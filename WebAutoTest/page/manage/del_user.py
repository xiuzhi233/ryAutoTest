"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : del_user.py
 @Author   : xiuzhi233
 @Time     : 2024/3/24 17:00
 @Describe : 
 
 
"""
import time
from WebAutoTest.page.login.loginPage import LoginPage


class UserManage(LoginPage):

    def __init__(self):
        super().__init__(browse_name="Chrome")
        # 1.登录
        self.login("admin", "admin123")
        # 2.点击【系统管理】
        self.click(self.yaml_data["manage"]["userManage"]["sysManage"])
        # 3.点击【用户管理】
        self.click(self.yaml_data["manage"]["userManage"]["userManage"])

    def add_user(self, nick_name, deptId=None, phonenumber=None, email=None, user_name, password=None, rolelds=None, status=None, postIds=None, sex=None):
        # 4.点击【新增】
        self.click(self.yaml_data["manage"]["userManage"]["addUser"])
        # 5.输入值
        self.send_keys(self.yaml_data["manage"]["userManage"]["nick_name"], nick_name)
        self.send_keys(self.yaml_data["manage"]["userManage"]["user_name"], user_name)
        # 6.保存
        self.click(self.yaml_data["manage"]["userManage"]["confirm"])
        time.sleep(2)
        # 7.获取返回的信息
        # response_text = self.presence(self.yaml_data["manage"]["userManage"]["response_text"]).text
        page = self.driver.page_source

        if "新增成功" not in page:
            self.click(self.yaml_data["manage"]["userManage"]["cancel"])

        return page


if __name__ == '__main__':
    user = UserManage()
    for i in range(2):
        print(user.add_user(nick_name=f"nick_name0{i + 1}", user_name=f"user_name0{i + 1}"))
        print(i+1)
        time.sleep(2)