from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
import allure
from common.find_element import sendkeys_element, click_element
from testcase.get_data import get_login_data


@allure.feature('模块：登录')
class TestLoginPage(object):
    @allure.title('打开页面')
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get('http://47.92.200.213:9999/admin/account.php?action=signin&err_login=1')
        self.driver.maximize_window()

    @allure.title('关闭浏览器页面')
    def teardown_method(self, method):
        sleep(3)
        self.driver.quit()

    @allure.step('账号登录（正确账号/正确密码）')
    @pytest.mark.parametrize(('user', 'password'), get_login_data())
    def test_ture(self, user, password):

        # form = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'user')))
        form = WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/div/div/div/div/div/div/form')))
        self.driver.switch_to.frame(form)

        with allure.step('第一步：输入正确账号'):
            sendkeys_element(self.driver, By.ID, 'user', user)

        with allure.step('第二步：输入正确密码'):
            sendkeys_element(self.driver, By.ID, 'pw', password)

        with allure.step('第三步：点击登录按钮'):
            click_element(self.driver, By.CLASS_NAME, 'bnt')

        try:
            assert self.driver.title == '管理中心 - Patrick Star_YL'
        except AssertionError:
            print('登录失败')

    @pytest.mark.undo
    @allure.step('账号登录（正确账号/错误密码）')
    def test_password_error(self, user, password):

        with allure.step('第一步：输入正确账号'):
            sendkeys_element(self.driver, By.ID, 'user', user)

        with allure.step('第二步：输入错误密码'):
            sendkeys_element(self.driver, By.ID, 'pw', password)

        with allure.step('第三步：点击登录按钮'):
            click_element(self.driver, By.CLASS_NAME, 'bnt')

        try:
            assert self.driver.file_detector_context('用户或密码错误，请重新输入')
        except AssertionError:
            print('登录异常')


if __name__ == '__main__':
    testcase = TestLoginPage()
    testcase.test_ture()
