"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : settings.py
 @Author   : xiuzhi233
 @Time     : 2024/3/9 14:27
 @Describe : 
 自定义配置文件，私有文件
 设置变量的默认值
"""

"""EXCEL列号配置"""

CASE_NUMBER = "A"                   # 用例编号
MODULE_NAME = "B"                   # 模块名称
API_NAME = "C"                      # 接口名称
CASE_TITLE = "D"                    # 用例标题
CASE_LEVEL = "E"                    # 用例等级
REQUEST_PATH = "F"                  # 请求路径
REQUEST_METHOD = "G"                # 请求方法
MIME = "H"                          # 媒体类型
CASE_DATA = "I"                     # 用例数据
EXPECT_DATA = "J"                   # 期望数据
SQL_TYPE = "K"                      # SQL语句类型
SQL_SENTENCE = "L"                  # SQL语句
UPDATE_KEY = "M"                    # 更新的KEY

"""INI文件节点"""

FILE = "FILE"                       # 数据文件（value为文件名）
TABLE = "TABLE"                     # excel sheet
HOST = "HOST"                       # 域名
MYSQL = "MYSQL"                     # 数据库连接信息

"""配置MYSQL节点的KEY"""

MYSQL_HOST = "MYSQL_HOST"           # 数据库域名
MYSQL_PORT = "MYSQL_PORT"           # 数据库端口
MYSQL_USER = "MYSQL_USER"           # 数据库用户名
MYSQL_PASSWORD = "MYSQL_PASSWORD"   # 数据库密码
MYSQL_DATABASE = "MYSQL_DATABASE"   # 数据库名称
