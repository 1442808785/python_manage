# import pytest
# import requests
# import allure
# import sys
# sys.dont_write_bytecode = True
#
# @allure.epic('测试描述'.center(30,'*'))
# @allure.feature('测试模块')
# @allure.suite('测试套件')
# class TestPytestOne():
#     @allure.story('用户故事描述:用例一')
#     @allure.title('测试标题:用例一')
#     @allure.description('测试用例描述:用例一')
#     @allure.testcase('测试用例地址:https://www.baidu.com/')
#     @allure.tag('测试用例标签:用例一')
#     def test_one(self):
#         print('执行第一个用例')
#         assert 1 == 1
#
#     @allure.story('用户故事描述:用例二')
#     @allure.title('测试标题:用例二')
#     @allure.description('测试用例描述:用例一')
#     @allure.testcase('测试用例地址:https://www.sogou.com/')
#     @allure.tag('测试用例标签:用例二')
#     def test_two(self,action):
#         print('执行第二个用例')
#         assert True == True
#
# if __name__ == "__main__":
#     pytest.main(['-s', '-v', 'test_Demo.py', '-q', '--alluredir', '../reports'])
