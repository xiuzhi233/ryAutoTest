"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : db.py
 @Author   : xiuzhi233
 @Time     : 2024/3/16 16:44
 @Describe : 
 
 
"""
import pymysql
from WebAutoTest.common.ReadIni import ReadIni


class DB:
    def __init__(self):
        """
        连接数据库，获取连接对象，创建游标对象
        """
        read_ini = ReadIni()
        try:
            # 根据ini文件配置信息，连接MySQL
            self.connect = pymysql.connect(
                host=read_ini.get_sql_connect("MYSQL_HOST"),
                port=int(read_ini.get_sql_connect("MYSQL_PORT")),
                user=read_ini.get_sql_connect("MYSQL_USER"),
                password=read_ini.get_sql_connect("MYSQL_PASSWORD"),
                database=read_ini.get_sql_connect("MYSQL_DATABASE"),
                charset="utf8"
            )
        except ConnectionError:
            raise ConnectionError("数据库连接错误，请检查配置文件！")
        else:
            # 获取游标对象
            self.cursor = self.connect.cursor()

    def select(self, sql_sentence):
        """
        执行查找的sql语句
        :param sql_sentence: sql语句
        :return:查询的结果
        """
        try:
            # 使用游标对象执行sql语句
            self.cursor.execute(sql_sentence)

        except ValueError:
            raise ValueError("请确认sql语句是否正确！")

        else:
            # 接收查询的结果
            select_result = self.cursor.fetchall()
            # 判断查询结果是否有数据
            if select_result:
                return select_result[0][0]
            else:
                return None

    def delete(self, sql_sentence):
        """执行删除的sql语句"""
        try:
            # 使用游标对象执行sql语句
            self.cursor.execute(sql_sentence)

        except ValueError:
            raise ValueError("请确认sql语句是否正确！")

        else:
            # 使用游标对象提交
            self.connect.commit()

    def close(self):
        self.cursor.close()
        self.connect.close()


if __name__ == '__main__':
    db = DB()
