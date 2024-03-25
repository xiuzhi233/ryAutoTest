"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : settings.py
 @Author   : xiuzhi233
 @Time     : 2024/3/16 20:02
 @Describe : 
 
 
"""

"""EXCEL列号配置"""

CASE_NUMBER = "A"                   # 用例编号
MODULE_NAME = "B"                   # 模块名称
FEATURE_NAME = "C"                  # 功能名称
CASE_TITLE = "D"                    # 用例标题
CASE_LEVEL = "E"                    # 用例等级
CASE_DATA = "F"                     # 用例数据
EXPECT_DATA = "G"                   # 期望数据
SQL_TYPE = "H"                      # SQL语句类型
SQL_SENTENCE = "I"                  # SQL语句
UPDATE_KEY = "J"                    # 更新的KEY

"""INI文件节点"""

FILE = "FILE"                       # 数据文件（value为文件名）
TABLE = "TABLE"                     # excel sheet
HOST = "HOST"                       # 域名
MYSQL = "MYSQL"                     # 数据库连接信息
REPORT = "REPORT"                   # 报告层
CASE_PATH = "CASE_PATH"             # 用例层

"""配置MYSQL节点的KEY"""

MYSQL_HOST = "MYSQL_HOST"           # 数据库域名
MYSQL_PORT = "MYSQL_PORT"           # 数据库端口
MYSQL_USER = "MYSQL_USER"           # 数据库用户名
MYSQL_PASSWORD = "MYSQL_PASSWORD"   # 数据库密码
MYSQL_DATABASE = "MYSQL_DATABASE"   # 数据库名称
