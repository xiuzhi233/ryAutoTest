"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : filepath.py
 @Author   : xiuzhi233
 @Time     : 2024/3/9 14:18
 @Describe : 
 
 
"""
from pathlib import Path

# 用于绑定项目文件位置的绝对路径(动态计算出来的)，所有文件夹都依赖于此路径
BASE_DIR = Path(__file__).resolve().parent.parent
print("123", BASE_DIR)
