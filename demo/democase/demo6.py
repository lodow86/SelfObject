from lib2to3.pgen2 import driver

from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/HTML.html'
        self.driver.get(file_path)
        self.driver.maximize_window()

    def get_selement(driver,*loc):
        e = driver.find_selement(*loc)
        return e

    def test_case(self):
        self.get_selement()
        self.get_selement(By.ID,'account').send_keys('hel')
        nanbox = self.get_selement(By.NAME, 'nan')
        if not nanbox.is_selected():
            nanbox.click()
        else:
            print('nanbox 已选中')
        self.get_selement(By.ID, 'password').send_keys('abcdefg')
        nvbox = self.get_selement(By.NAME, 'nv')
        if not nvbox.is_selected():
            nvbox.click()
        else:
            print(' nvbox被选中')
        sleep(10)
        self.get_selement(By.ID,'submit').click()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(5)


if __name__ == '__main__':
    case = TestCase()
    case.test_case()

