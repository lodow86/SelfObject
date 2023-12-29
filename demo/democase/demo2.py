from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 类下初始化驱动路线，定义两个方法
class Testpage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        sleep(2)
    def test_id(self):
        element=self.driver.find_element(By.ID,'kw')
        element.send_keys('bilibili')
        print(type(element))
        # self.driver.quit()

    def test_id2(self):
        self.test_id()
        me = self.driver.find_element(By.ID,'su')
        me.click()
        sleep(2)
        print(type(me))
        self.driver.quit()


if __name__ =='__main__':
    case =Testpage()
    case.test_id2()
