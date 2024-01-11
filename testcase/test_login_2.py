from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
import allure
from common.Basecase import sendkeys_element, click_element, save_screenshot
from common.Datacase import login_data


@allure.feature('模块：登录')
class TestLoginPage(object):
    @pytest.mark.parametrize('url', login_data())
    @allure.title('打开页面')
    def setup_method(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(str(url))

    @allure.title('关闭浏览器页面')
    def teardown_method(self):
        sleep(2)
        self.driver.quit()

    @staticmethod
    def data():
        res = '登录成功'
        error_res = '用户或密码错误，请重新输入'
        ture_user = 'Aa'
        ture_password = 'Aa123456'
        error_user = 'A'
        error_password = 'A'
        return ture_user, ture_password, res, error_res

    # @allure.step('账号登录（正确账号/正确密码）')
    @allure.testcase(url='http://47.92.200.213:9999/admin/account.php?action=signin', name='校验登录正确账号正确密码')
    @pytest.mark.parametrize(('ture_user', 'ture_password', 'res', 'error_res'), [data()])
    def test_ture(self, url, ture_user, ture_password, res, error_res):

        with allure.step('第一步：输入正确账号'):
            sendkeys_element(self.driver, By.ID, 'user', ture_user)

        with allure.step('第二步：输入正确密码'):
            sendkeys_element(self.driver, By.ID, 'pw', ture_password)

        with allure.step('第三步：点击登录按钮'):
            click_element(self.driver, By.CLASS_NAME, 'btn')

        with allure.step('第四步：截图'):
            save_screenshot(self.driver)

        try:
            assert self.driver.title == '管理中心 - Patrick Star_YL'
            print(res)
        except AssertionError:
            print(error_res)

    # @pytest.mark.undo
    # @allure.step('账号登录（正确账号/正确密码）')
    # @pytest.mark.parametrize(('module', 'title', 'user', 'password', 'res'), get_login_data())
    # def test_ture(self, user, password):
    #
    #     with allure.step('第一步：输入正确账号'):
    #         sendkeys_element(self.driver, By.ID, 'user', user)
    #
    #     with allure.step('第二步：输入正确密码'):
    #         sendkeys_element(self.driver, By.ID, 'pw', password)
    #
    #     with allure.step('第三步：点击登录按钮'):
    #         click_element(self.driver, By.CLASS_NAME, 'btn')
    #
    #     with allure.step('第四步：截图'):
    #         save_screenshot(self.driver)
    #
    #     try:
    #         assert self.driver.file_detector_context('用户或密码错误，请重新输入')
    #     except AssertionError:
    #         print('登录异常')


if __name__ == '__main__':
    pytest.main(['--alluredir', './reports', '-sv', 'test_login_2.py'])
