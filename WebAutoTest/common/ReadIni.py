"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : ReadIni.py
 @Author   : xiuzhi233
 @Time     : 2024/3/16 10:37
 @Describe : 
 
 
"""
import configparser
import os


class ReadIni:

    def __init__(self):
        """获取ini文件路径"""
        self.project_path = os.path.dirname(os.path.dirname(__file__))
        self.data_config_path = os.path.join(self.project_path, 'data_config')
        ini_path = os.path.join(self.data_config_path, 'config.ini')
        self.conf = configparser.ConfigParser()
        self.conf.read(ini_path, encoding="utf-8")

    def get_file_path(self, key):
        """
        根据key获取FILE节点下文件的路径
        :param key:
        :return:
        """
        try:
            file_name = self.conf.get("FILE", key)
        except KeyError:
            raise KeyError("根据key获取FILE节点下文件的路径-->传入的key错误!")
        else:
            return os.path.join(self.data_config_path, file_name)

    def get_table_name(self, key):
        """
        根据key获取TABLE节点下的路径
        :param key:
        :return:
        """
        try:
            table_name = self.conf.get("TABLE", key)
        except KeyError:
            raise KeyError("根据key获取TABLE节点下文件的路径-->传入的key错误!")
        else:
            return table_name

    def get_host(self, key):
        """
        根据key获取HOST节点下的值
        :param key:
        :return:
        """
        try:
            host = self.conf.get("HOST", key)
        except KeyError:
            raise KeyError("根据key获取HOST节点下的值-->传入的key错误!")
        else:
            return host

    def get_sql_connect(self, key):
        """
        根据key获取MYSQL节点下的连接信息
        :param key:
        :return:
        """
        try:
            value = self.conf.get("MYSQL", key)
        except KeyError:
            raise KeyError("根据key获取MYSQL节点下的连接信息-->传入的key错误!")
        else:
            return value

    def get_report_path(self, key):
        """
        根据key获取REPORT节点下的路径
        :param key:
        :return:
        """
        try:
            report_name = self.conf.get("REPORT", key)
        except KeyError:
            raise KeyError("根据key获取REPORT节点下的路径-->传入的key错误!")
        else:
            report_path = os.path.join(self.project_path, "report")
            return os.path.join(report_path, report_name)

    def get_case_path(self, key):
        """
        根据key获取CASE_PATH节点下的路径
        :param key:
        :return:
        """
        try:
            test_case_path = self.conf.get("CASE_PATH", key)
        except KeyError:
            raise KeyError("根据key获取CASE_PATH节点下的路径-->传入的key错误!")
        else:
            return os.path.join(self.project_path, test_case_path)


if __name__ == '__main__':
    read = ReadIni()
    path = read.get_case_path("TEST_CASE")
    for item in os.scandir(path):
        print((os.path.abspath(__file__)))
