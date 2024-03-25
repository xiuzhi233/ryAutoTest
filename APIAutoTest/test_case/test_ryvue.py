"""
 -*- coding: utf-8 -*-
 @Project  : ryvueAutoTest
 @File     : test_ryvue.py
 @Author   : xiuzhi233
 @Time     : 2024/2/19 19:38
 @Describe : 
 
 
"""
import logging
import pytest
import allure

from APIAutoTest.common import log_decorator
from APIAutoTest.common.ReadExcel import ReadExcel


class TestRyvue:
    @allure.epic("若依接口自动化测试")
    @log_decorator
    @pytest.mark.parametrize(
        "case_number, module_name, api_name, case_title, case_level, request_url, request_method, request_mime, "
        "request_data, request_expect, sql_type, sql_sentence, update_key",
        ReadExcel().get_data())
    def test_ryvue(self, db_fixture, request_fixture, case_number, module_name, api_name, case_title, request_url,
                   case_level, request_method, request_mime, request_data, request_expect, sql_type, sql_sentence,
                   update_key):
        # 调用allure功能，影响报告的显示
        # @allure.feature("模块名称")
        allure.dynamic.feature(module_name)
        # @allure.story("接口名称")
        allure.dynamic.story(api_name)
        # @allure.title("用例标题")
        allure.dynamic.title(case_title)
        # @allure.severity("用例等级")
        allure.dynamic.severity(case_level)
        # 判断sql语句类型是否为DELETE
        if sql_type == "DELETE":
            # 使用DB类对象来执行删除的语句
            db_fixture.delete(sql_sentence)

        elif sql_type == "SELECT":
            # 使用DB类对象来执行查询的语句，接收查询的结果
            select_result = db_fixture.select(sql_sentence)
            # 将查询结果更新到用例数据中
            request_data[update_key] = select_result
            # 更新之后的用例数据发送给服务器

        elif sql_type == "SELECT|DELETE" or sql_type == "DELETE|SELECT":
            # 使用DB类对象，调用delete方法执行删除语句；使用DB类对象来执行查询的语句，接收查询的结果
            db_fixture.delete(sql_sentence.get("DELETE"))
            select_result = db_fixture.delete(sql_sentence.get("SELECT"))
            request_data[update_key] = select_result

        # 使用RequestMethod对象发送请求
        response = request_fixture.request_all(req_method=request_method, req_url=request_url, req_mime=request_mime,
                                               case_data=request_data)
        allure.dynamic.description(f"actual_data:{response.json()}")
        # 断言
        try:
            # 获取期望数据的key，期望数据的key对应的值是否和服务器返回的数据key对应的值相等，如果相等断言成功，否则失败
            # assert response.json().get('msg') == request_expect['msg']
            # and response.json().get('code') == request_expect['code']

            for key in request_expect.keys():
                assert response.json().get(key) == request_expect[key]

        except AssertionError:
            logging.error(case_number + "断言失败，用例数据为：" + str(request_data) + "期望数据为：" + str(
                request_expect) + "服务器返回的期望数据：" + response.text)
            raise AssertionError("断言失败")

        else:
            print("断言成功")


if __name__ == '__main__':
    r"""
    运行
    删除allure_json和AllureReport
    pytest .\test_case\ --alluredir=./report/allure_json --clean-alluredir
    allure generate .\report\allure_json\ -o .\report\AllureReport
    allure open ./report/AllureReport
    """
    pytest.main()
