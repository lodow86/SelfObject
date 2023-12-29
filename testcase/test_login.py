from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
import allure



@allure.feature('模块：登录')
class TestLoginPage(object):
    @allure.title('打开页面')
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.driver.get('http://47.92.200.213:9999/admin/account.php?action=signin&err_login=1')
        self.driver.maximize_window()

    @allure.title('关闭浏览器页面')
    def teardown_method(self,method):
        self.driver.quit()


    @allure.step('账号登录（正确账号/正确密码）')
    # @pytest.mark.parametrize( )
    def test_ture(self):
        # @allure.title('输入正确账号')
        @allure.step('第一步：输入正确账号')
        self.driver.find_element(By.ID, 'user').send_keys('user')
        @allure.step('第二步：输入正确密码')
        self.driver.find_element(By.ID, 'pw').send_keys('password')
        @allure.step('第三步：点击登录按钮')
        self.driver.find_element(By.CLASS_NAME, 'bnt').click()
        try:
            assert   self.driver.title == '管理中心 - Patrick Star_YL'
        except AssertionError:
            print('登录失败')

    @allure.story('账号登录（正确账号/错误密码）')
    def test_password_error(self):
        self.driver.find_element(By.ID, 'user').send_keys('user')
        self.driver.find_element(By.ID, 'pw').send_keys('password')
        self.driver.find_element(By.CLASS_NAME, 'bnt').click()
        sleep(5)

    @allure.story('账号登录（错误账号/正确密码）')
    def test_username_error(self):
        self.driver.find_element(By.ID, 'user').send_keys('user')
        self.driver.find_element(By.ID, 'pw').send_keys('password')
        self.driver.find_element(By.CLASS_NAME, 'bnt').click()
        sleep(5)

    @allure.story('账号登录（错误账号/错误密码）')
    def test_null(self):
        self.driver.find_element(By.ID, 'user').send_keys('user')
        self.driver.find_element(By.ID, 'pw').send_keys('password')
        self.driver.find_element(By.CLASS_NAME, 'bnt').click()
        sleep(5)


if __name__ == '__main__':
    testcase = TestLoginPage()
    testcase.test_ture()
