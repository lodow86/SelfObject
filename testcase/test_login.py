from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import allure
from common.Basecase import sendkeys_element, click_element, save_screenshot
from common.get_data import get_login_data


@allure.feature('模块：登录')
class TestLoginPage(object):
    @pytest.fixture(scope='class')  # 声明fixture夹具为类级别
    def setup_teardown(self):
        """执行前运行"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        yield

        """执行后运行"""
        self.driver.quit()

    @pytest.fixture(scope='module')    #声明为模块级别
    def setup_teardown_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://47.92.200.213:9999/admin/account.php?action=signin')

        yield

        sleep(2)
        # self.driver.close()

    @allure.testcase('http://47.92.200.213:9999/admin/account.php?action=signin', name='登录测试用例')
    @pytest.mark.parametrize(('user', 'password', 'res', 'error'), get_login_data())
    def test_ture(self, setup_teardown_method, user, password, res, error):

        with allure.step('第一步：输入正确账号'):
            sendkeys_element(self.driver, By.ID, 'user', user)

        with allure.step('第二步：输入正确密码'):
            sendkeys_element(self.driver, By.ID, 'pw', password)

        with allure.step('第三步：点击登录按钮'):
            click_element(self.driver, By.CLASS_NAME, 'btn')

        with allure.step('第四步：截图'):
            save_screenshot(self.driver, '登录成功')

        try:
            assert self.driver.title == '管理中心 - Patrick Star_YL'
            print(res)
        except AssertionError:
            print(error)


if __name__ == '__main__':
    pytest.main(['--alluredir', './reports', '-vs', 'test_login.py'])
