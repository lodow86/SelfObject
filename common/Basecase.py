from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
from datetime import datetime
from selenium.webdriver import ActionChains as AC, Keys

'''寻找元素方法'''


def find_element(driver, by, locator):
    """
    :param driver:  对象
    :param by: 定位方式
    :param locator: 定位器
    :return:返回元素
    """
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((by, locator)))
        return element
    except TimeoutError:
        print(f'元素定位失败：{by}={locator}')


'''元素单击'''


def click_element(driver, by, locator):
    element = find_element(driver, by, locator)
    element.click()


'''输入字符'''


def sendkeys_element(driver, by, locator, value):
    element = find_element(driver, by, locator).send_keys(value)


''''图片记录'''


def save_screenshot(driver, value):
    screenshot_name = datetime.now().strftime('%Y-%m-%d-%H-%M') + value + '.png'  # 通过datetime获取现在时间并整数赋值
    path = os.path.dirname(os.path.abspath(__file__))  # 获取绝对路径
    screenshot_path = os.path.join(path, '..', 'screenshot')  # 截图保存路径
    file_path = os.path.join(screenshot_path, screenshot_name)  # 截图存放
    driver.save_screenshot(file_path)  # 保存截图

