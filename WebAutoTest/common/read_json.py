"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : read_json.py
 @Author   : xiuzhi233
 @Time     : 2024/3/16 16:52
 @Describe : 
 
 
"""
import json
import os


def read_json(filepath):
    """
    根据文件路径，读取json文件，将json文件的数据转成python对象并返回
    :param filepath:
    :return:
    """
    # 读之前判断路径合法
    if os.path.isfile(filepath) and filepath.endswith(".json"):
        with open(filepath, mode='r', encoding="utf-8") as f:
            try:
                value = json.load(f)
            except FileExistsError:
                raise FileExistsError("json文件数据编解码错误！")
            else:
                return value
    else:
        raise FileNotFoundError("json文件路径错误！")


if __name__ == '__main__':
    datas = read_json(r'X:\CodeAndProjects\Python\ryvueAutoTest\WebAutoTest\data_config\sql_data.json')
    print(datas["用户管理"]["添加用户"]["add_user_001"])
