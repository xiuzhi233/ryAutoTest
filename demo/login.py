"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : get_ryvue
 @Author   : xiuzhi233
 @Time     : 2023/12/8 10:36
 @Describe : 
 
 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 创建实例化对象
driver = webdriver.Chrome()

ry_admin_url = "http://192.168.109.134:81/"

driver.maximize_window()

# 隐式等待
driver.implicitly_wait(5)

driver.get(ry_admin_url)

# 显式等待
WebDriverWait(driver, 5, 0.3).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/form/div[1]/div/div[1]/input'))).send_keys("admin")

WebDriverWait(driver, 5, 0.3).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/form/div[2]/div/div[1]/input'))).send_keys(
    "admin123")

WebDriverWait(driver, 5, 0.3).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/form/div[3]/div/button'))).click()

# 用户管理
WebDriverWait(driver, 5, 0.3).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span'))).click()

WebDriverWait(driver, 5, 0.3).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li'))).click()

WebDriverWait(driver, 5, 0.3).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[1]/div[2]/section/div/div[1]/div[2]/div[1]/div[1]/button'))).click()