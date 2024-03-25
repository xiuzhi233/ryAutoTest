"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : ReadIni.py
 @Author   : xiuzhi233
 @Time     : 2024/2/19 10:05
 @Describe : 
 读取ini文件
 
"""
import configparser
import os


class ReadIni:
    def __init__(self):
        """获取ini文件的路径，创建configparser对象，并读取ini文件"""

        """
        1、先获取当前文件的路径，__file__
        2、获取当前文件的目录，parent_dir = os.path.dirname(os.path.dirname(__file__))
        3、获取dataconfig目录路径，dataconfig_path = os.path.join(parent_dir, "data_config")
        4、获取login目录路径，login_path = os.path.join(dataconfig_path, "login")
        5、获取ini文件的路径，
        """
        # 当前文件的目录
        self.parent_dir = os.path.dirname(os.path.dirname(__file__))
        
        # dataconfig文件的路径
        self.dataconfig_path = os.path.join(self.parent_dir, "data_config")
        
        # ini文件的路径
        ini_path = os.path.join(self.dataconfig_path, "config.ini")

        # 创建configparser对象
        self.configparser = configparser.ConfigParser()

        # 用configparser读取ini
        self.configparser.read(ini_path, encoding="utf-8")

    def get_file_path(self, key):
        """
        获取ini文件中，节点下的文件绝对路径
        :param key:[file]节点下的key
        :return:文件的路径
        """
        # 获取key的值
        try:
            file_name = self.configparser.get("FILE", key)
        except KeyError:
            raise KeyError("ini文件下FILE节点传入的key错误！")
        else:
            # 拼接路径并返回
            return os.path.join(self.dataconfig_path, file_name)

    def get_table_name(self, key):
        """
        根据key获取工作表sheet名称
        :param key:[table]节点下的key
        :return:工作表名称
        """
        try:
            sheet = self.configparser.get("TABLE", key)
        except KeyError:
            raise KeyError("ini文件下TABLE节点传入的key错误！")
        else:
            return sheet

    def get_host(self, key):
        """
        根据key获取host域名
        :param key: [HOST]
        :return: host地址
        """
        try:
            host = self.configparser.get("HOST", key)
        except KeyError:
            raise KeyError("ini文件下HOST节点传入的key错误！")
        else:
            return host

    def sql_connect(self, key):
        """
        根据key获取数据库的连接信息
        :param key:
        :return:
        """
        try:
            message = self.configparser.get('MYSQL', key)
        except KeyError:
            raise KeyError("ini文件下MYSQL节点传入的key错误！")
        else:
            return message


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.sql_connect("host"), type(read_ini.sql_connect("host")))