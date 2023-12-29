from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class TestPage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
    def Test(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID,'kw').send_keys('BILIBILI')
        time.sleep(1)
        self.driver.find_element(By.ID,'su').click()
        time.sleep(5)
        self.driver.quit()
    # def test2(self):
    #     # self.driver = webdriver.Chrome()
    #     self.driver.get('https://www.baidu.com/')
    #     self.driver.find_element(By.ID, 'kw').send_keys('BILIBILI')
    #     time.sleep(3)
    #     self.driver.find_element(By.ID, 'su').click()
    #     time.sleep(3)
    #     self.driver.find_element(By.PARTIAL_LINK_TEXT,'干杯~-bilibili').click()
    #     time.sleep(3)
    #     self.driver.quit()

if __name__ == '__main__':
    case = TestPage()
    case.Test()
    print('测试完毕')