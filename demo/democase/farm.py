from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/framesTest.htm')

    def test1(self):
        top = self.driver.find_element(By.NAME, 'top')
        self.driver.switch_to.frame(top)                                                        #切换到表单内
        self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
        time.sleep(1)
        self.driver.switch_to.default_content()                                                 #切出表单
        self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[3]').click()
        time.sleep(1)


if __name__ == '__main__':
    case = TestCase()
    case.test1()
