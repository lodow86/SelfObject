from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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


def click_element(driver, by, locator):
    element = find_element(driver, by, locator)
    element.click()


def sendkeys_element(driver, by, locator, value):
    element = find_element(driver, by, locator)
    element.send_keys(value)

