"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : add_role.py
 @Author   : xiuzhi233
 @Time     : 2024/3/29 16:20
 @Describe : 
 
 
"""
import time

from WebAutoTest.page.login.loginPage import LoginPage


class RoleManage(LoginPage):
    def __init__(self):
        super().__init__(browse_name="Chrome")
        # 1.登录
        self.login("admin", "admin123")
        # 2.点击系统管理
        self.click(self.yaml_data["manage"]["roleManage"]["sysManage"])
        # 3.点击角色管理
        self.click(self.yaml_data["manage"]["roleManage"]["roleManage"])

    def add_role(self, roleName, roleKey, roleSort, status, menuIds, remark):
        """

        :param roleName: 角色名称
        :param roleKey: 权限字符
        :param roleSort: 角色顺序
        :param status: 状态
        :param menuIds: 菜单权限
        :param remark: 备注
        :return: page
        """
        # 4.点击新增
        self.click(self.yaml_data["manage"]["roleManage"]["addRole"])
        # 5.输入角色名称
        self.send_keys(self.yaml_data["manage"]["roleManage"]["roleName"], roleName)
        # 6.输入权限字符
        self.send_keys(self.yaml_data["manage"]["roleManage"]["roleKey"], roleKey)
        # 7.输入角色顺序
        self.send_keys(self.yaml_data["manage"]["roleManage"]["roleSort"], roleSort)
        # 8.状态
        if status == 0:
            self.click(self.yaml_data["manage"]["roleManage"]["status_0"])
        else:
            self.click(self.yaml_data["manage"]["roleManage"]["status_1"])
        # 9.菜单权限
        if menuIds == "manage":
            self.click(self.yaml_data["manage"]["roleManage"]["menuIds_manage"])
        elif menuIds == "control":
            self.click(self.yaml_data["manage"]["roleManage"]["menuIds_control"])
        elif menuIds == "tool":
            self.click(self.yaml_data["manage"]["roleManage"]["menuIds_tool"])
        # 10.备注
        self.send_keys(self.yaml_data["manage"]["roleManage"]["remark"], remark)
        # 11.确定
        self.click(self.yaml_data["manage"]["roleManage"]["confirm"])
        time.sleep(1)
        page = self.driver.page_source

        if "新增成功" not in page:
            self.click(self.yaml_data["manage"]["roleManage"]["cancel"])
        return page


if __name__ == '__main__':
    role = RoleManage()
    print(role.add_role("add_role_02", "admin", "1", "1", "manage", "remark"))
