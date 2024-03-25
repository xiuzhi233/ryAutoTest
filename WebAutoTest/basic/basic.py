"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : basic.py
 @Author   : xiuzhi233
 @Time     : 2024/3/16 20:30
 @Describe : 
 对定位方式进行封装，对元素的操做方式进行二次封装
 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from WebAutoTest.common.ReadIni import ReadIni
from WebAutoTest.data_config.settings import *


class Basic:
    def __init__(self, browse_name="Chrome"):
        """
        判断浏览器的类型，启动driver
        :param browse_name:
        """
        if browse_name == "Chrome" or browse_name == "chrome" or browse_name == "c" or browse_name == "C":
            self.driver = webdriver.Chrome()

        elif browse_name == "Edge" or browse_name == "edge" or browse_name == "e" or browse_name == "E":
            self.driver = webdriver.Edge()

        elif browse_name == "firefox" or browse_name == "Firefox" or browse_name == "f" or browse_name == "F":
            self.driver = webdriver.Firefox()

        else:
            raise NameError("浏览器的名称传入错误！")

        # 窗口最大化
        self.driver.maximize_window()

        # 获取访问的URL
        self.read_ini = ReadIni()
        self.driver.get(self.read_ini.get_host(HOST))

    @staticmethod
    def selector_and_locator(strs):
        """
        二次封装定位方式
        :param strs:
        :return:
        """
        # locator -> “定位类型, 定位的值” -> yaml文件
        selector = strs.split(",")[0].strip()    # 定位类型
        locator = strs.split(",")[1].strip()     # 定位的值
        # 下面是定位的二次封装，判断selector的值（八大定位）

        # ID = "id"
        if selector in ['css', 'css_selector', 'CSS_SELECTOR']:
            return By.CSS_SELECTOR, locator
        # XPATH = "xpath"
        elif selector in ['xpath', 'XPATH']:
            return By.XPATH, locator
        # LINK_TEXT = "link text"
        elif selector in ['link_text', 'LINK_TEXT']:
            return By.LINK_TEXT
        # PARTIAL_LINK_TEXT = "partial link text"
        elif selector in ['partial link text', 'PARTIAL_LINK_TEXT']:
            return By.PARTIAL_LINK_TEXT
        # NAME = "name"
        elif selector in ['name', 'NAME']:
            return By.NAME
        # TAG_NAME = "tag name"
        elif selector in ['tag_name', 'TAG_NAME']:
            return By.TAG_NAME
        # CLASS_NAME = "class name"
        elif selector in ['class_name', 'CLASS_NAME']:
            return By.CLASS_NAME
        # CSS_SELECTOR = "css selector"
        elif selector in ['css', 'css_selector', 'CSS_SELECTOR']:
            return By.CSS_SELECTOR, locator
        else:
            raise NameError("传入的定位方式错误")

    def presence(self, strs):
        """
        根据传入的字符串，进行元素出现之后的定位
        :param strs:
        :return:
        """
        selector_result = self.selector_and_locator(strs)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(selector_result))

    def send_keys(self, locators, value):
        """
        传入值的操做
        :param locators:
        :param value:
        :return:
        """
        element = self.presence(locators)
        element.send_keys(value)

    def clickable(self, strs):
        """
        根据传入的字符串，获取元素是否可点击
        :param strs:
        :return:
        """
        element_locator = self.selector_and_locator(strs)
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element_locator))

    def click(self, locators):
        """
        点击操做
        :param locators:元素的定位方式（字符串）
        :return:
        """
        element = self.clickable(locators)
        element.click()

    def close(self):
        self.driver.quit()

    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    bas = Basic()
    print(bas.selector_and_locator('XPATH, //*[@id="app"]/div[1]/form/div[1]/div/div/input'))
    time.sleep(2)
