from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


'''封装元素的使用方法，'''
def get_element(driver, *loc):     # 定义需要元素的方法   *loc表示所有元素
    e = driver.find_element(*loc)
    return e


if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.get('https://www.baidu.com/')
    sleep(1)
    get_element(dr, By.ID, 'kw').send_keys('bilibili') #  元素*loc赋值 By.ID,'kw'
    get_element(dr, By.ID, 'su').click()
