"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : read_yaml.py
 @Author   : xiuzhi233
 @Time     : 2024/3/16 16:55
 @Describe : 
 
 
"""
import yaml
import os


def read_yaml(filepath):
    """
    根据文件路径，读取yaml文件，将yaml文件的数据转成python对象并返回
    :param filepath:
    :return:
    """
    # 读之前判断路径合法
    if os.path.isfile(filepath) and filepath.endswith(".yaml"):
        with open(filepath, mode='r', encoding="utf-8") as f:
            try:
                value = yaml.load(f, Loader=yaml.FullLoader)
            except FileExistsError:
                raise FileExistsError("yaml文件数据编解码错误！")
            else:
                return value
    else:
        raise FileNotFoundError("yaml文件路径错误！")


if __name__ == '__main__':
    print(read_yaml(r'X:\CodeAndProjects\Python\ryvueAutoTest\WebAutoTest\data_config\locator.yaml'))
