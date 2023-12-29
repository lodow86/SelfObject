import os.path
from time import sleep, strftime
from selenium import webdriver
from datetime import datetime
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')
        sleep(2)

    def save_picture(self):
        # curr_time = datetime.now()
        # timestamp = datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
        # print(timestamp)
        # st = datetime.time("%Y-%m-%d %H:%S:%M")
        # st = strftime("%Y-%m-%d %H:%S:%M",localtime(time()))
        t2 = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")               #本地时间转换为str
        filename = t2 + '.png'
        # self.driver.save_screenshot(filename)
        path = os.path.abspath('../pictrue')                                #目录abs绝对路径
        file_path = path + '/' + filename                                 #相对路径
        self.driver.save_screenshot(file_path)


if __name__ == '__main__':
    case = TestCase()
    # case.test_case()
    case.save_picture()
