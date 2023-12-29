import pytest
import allure


@pytest.fixture(scope='session')
def login():
    print('登录成功')


@allure.step('步骤一：获取元素')
def step_01():
    print('寻找元素')


@allure.step('步骤二：添加文章')
def step_02():
    print('添加文章')


@allure.step('步骤三：点击链接')
def step_03():
    print('点击链接')


@allure.feature('文章编辑页面')
class TestAddPage():
    """ 编辑页面 """

    @allure.story('新增加文章')
    def test_01(self, login):
        step_01()
        step_02()
        print('添加文章成功')

    @allure.story('跳转链接')
    def test_02(self, login):
        step_01()
        step_03()
        print('跳转链接')


if __name__ == '__main__':
    pytest.main()
    # ['--alluredir', './reports', 'test_allure.py']
    # pytest - -alluredir  E:\UI\DEMO0\reports E:\UI\DEMO0\testcase\test_allure.py    #命令： pytest 驱动 报告存放路径 用例路径
    # allure serve.\reports     #将json报告转化为HTML

