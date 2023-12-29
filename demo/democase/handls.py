from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# 窗口切换
class Testpage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.get('https://www.baidu.com/')
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()

    def test_prop(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '新闻').click()
        sleep(3)
        # print(self.driver.current_window_handle)
        wind = self.driver.current_window_handle
        winds = self.driver.window_handles
        windows =self.driver.window_handles
        for s in windows:
            self.driver.switch_to.window(s)         #切换窗口句柄
        sleep(3)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'hao123').click()
        sleep(3)
        print(self.driver.window_handles)           #获取窗口句柄

        # self.driver.find_element(By.XPATH, '//*[@id="pane-news"]/div/ul/li[1]/strong/a').click()
        # print(self.driver.current_window_handle)
        # handle = self.driver.window_handles
        # print('窗口'.format(handle))

        # self.driver.find_element(By.PARTIAL_LINK_TEXT, 'hao123').click()
        # windons = self.driver.window_handles
        # while 1:
        #     for w in windons:
        #         self.driver.switch_to.window(w)
        #     else:
        #         self.driver.switch_to.window()




        # self.driver.find_element(By.ID,'kw').send_keys('中燃')
        # self.driver.find_element(By.ID,'su').click()
        # sleep(2)
        # self.driver.back()
        # sleep(2)
        # self.driver.refresh()
        # self.driver.forward()
        # self.driver.back()
        # sleep(1)
        # print(self.driver.name) #浏览器名称
        # print(self.driver.current_url)  #目前的url
        # print(self.driver.title)        #获取到现在的title，常用于断言
        # print(self.driver.window_handles)   #获取窗口
        # self.driver.quit()

    def test_element_proo(self):
        e = self.driver.find_element(By.ID, 't1')
        e.send_keys('天加')
        # print(type(e))
        # e1 = WebElement
        # print(e.id)
        # print(e.tag_name)
        # print(e.text)
        sleep(2)
        print(e.get_attribute('name'))
        print(e.get_attribute('type'))
        print(e.get_attribute('value'))
        self.driver.quit()


if __name__ == '__main__':
    case = Testpage()
    case.test_prop()
    # case.test_element_proo()
