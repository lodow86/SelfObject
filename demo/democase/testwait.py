from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        sleep(2)

    def implicitly_test(self):
        self.driver.implicitly_wait(10)                                 #隐形等待
        element = self.driver.find_element(By.ID, 'kw')
        element.send_keys('bilibili')
        me = self.driver.find_element(By.ID, 'su')
        me.click()

    def test_wait(self):
        wait = WebDriverWait(self.driver, 2)                    #显性等待
        wait.until(EC.title_is('百度一下，你就知道'))
        element = self.driver.find_element(By.ID, 'kw')
        element.send_keys('bilibili')
        me = self.driver.find_element(By.ID, 'su')
        me.click()


if __name__ == '__main__':
    case = TestPage()
    # case.implicitly_test()
    case.test_wait()
    # webdriver.Chrome().quit()
