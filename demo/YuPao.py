"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : YuPao.py
 @Author   : xiuzhi233
 @Time     : 2024/3/11 15:15
 @Describe : 
 
 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 创建实例化对象
driver = webdriver.Chrome()

target_url = "https://www.yupao.com/"

driver.maximize_window()

# 隐式等待
driver.implicitly_wait(5)

driver.get(target_url)

driver.maximize_window()

time.sleep(5)
