"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : read_json.py
 @Author   : xiuzhi233
 @Time     : 2024/2/19 11:24
 @Describe : 
 读取json文件
 
"""
import json
import os.path


def read_json(filepath):
    """
    根据文件路径读取json文件，并将json文件中的数据转成python文件对象，再返回
    :param filepath:json文件路径
    :return:python文件对象
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
    json_path = r'X:\CodeAndProjects\Python\ryvueAutoTest\APIAutoTest\data_config\expect_data.json'
    print(read_json(json_path))
