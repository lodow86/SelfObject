from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

'''选择框下拉枚举选择'''


class Testpage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        xpath = 'file:///' + path + '/HTML.html'
        self.driver.get(xpath)

    def test_page(self, ):
        se = self.driver.find_element(By.ID, 'name')
        select = Select(se)
        '''单选下拉'''
        # select.select_by_index(3)                               #根据0123选择
        # sleep(2)
        # select.select_by_value('AF')                            #根据value参数选择
        # sleep(2)
        # select.select_by_visible_text('1')                      #根据可见文本选择
        # sleep(2)
        '''多选下来'''
        for x in range(5):                                         #for循环5次 每次都选择
            select.select_by_index(x)
            sleep(2)
        sleep(3)
        select.deselect_all()                                       #反选
        sleep(2)
        for options in select.options:
            print(options.text)



if __name__ == '__main__':
    case = Testpage()
    case.test_page()
