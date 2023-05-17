import pytest
import allure

@allure.feature('列表模块')
class TestDemo(object):
    @allure.story('列表')
    def test_num(self):
        list = ['a', 'b', 'c', 'd', 'e']
        n = len(list)
        login(list, n)
        with allure.step("计算长度"):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach('列表', '长度')  # attach可以打印一些附加信息
        assert n == 5

@allure.step('步骤一')
def login(list, size):
    print(list, size)

