from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.common.by import By

#os 引用dirname 设置本地路径
class TestCase(object):
    def __init__(self):
        # self.driver = webdriver.chrome()
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))   # 根目录嵌abs路径
        file_path = 'file:///' + path + '/HTML.html'    # 路径赋值
        self.driver.get(file_path)

    def test_case(self):
        username = self.driver.find_element(By.ID, 'account')
        username.send_keys('account')
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys('pws')
        sleep(2)
        submit = self.driver.find_element(By.ID, 'submit')
        submit.click()
        sleep(2)
        self.driver.switch_to.alert.accept() # alert.accept                     --     弹窗接受
        self.driver.switch_to.alert.dismiss()               # alert.dismiss   取消
        username.clear()
        sleep(2)

        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_case()
