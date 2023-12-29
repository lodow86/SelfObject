from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver, by, locator):
    """
    :param driver:  对象
    :param by: 定位方式
    :param locator: 定位器
    :return:/
    """
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((by, locator)))
    return element


def click_element(driver, by, locator):
    element = find_element(driver, by, locator)
    element.click()


def sendkeys_element(driver, by, locator, vaule):
    element = find_element(driver, by, locator)
    element.send_keys(vaule)
