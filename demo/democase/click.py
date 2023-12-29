from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.get('https://sahitest.com/demo/clicks.htm')

    def test_case(self):
        bnt = self.driver.find_elements(By.XPATH, '/html/body/form/input[2]')
        AC = ActionChains(self.driver)
        AC.double_click(bnt).perform()
        sleep(2)
        sc = self.driver.find_elements(By.XPATH, '/html/body/form/input[3]')
        AC.click(sc).perform()
        sleep(2)
        js = self.driver.find_elements(By.XPATH, '/html/body/form/input[4]')
        AC.context_click(js).perform()
        sleep(2)

    def test_case2(self):
        self.driver.get('https://www.baidu.com/')
        element = self.driver.find_element(By.ID, 'kw')
        element.send_keys('bilibili')
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.CONTROL, 'x')
        element.send_keys(Keys.CONTROL, 'v')
        # self.driver.back()
        sleep(2)
        # old = self.driver.current_window_handle                               #切换窗口
        # new = self.driver.window_handles
        # for handle in new:
        #     if old != handle:
        #         self.driver.switch_to.window(old)
        # sleep(5)
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, '新闻')
        ActionChains(self.driver).move_to_element(element).click().perform()        #移动到元素上并点击
        sleep(5)
        # wait = WebDriverWait(self.driver, 2)                                  #显式等待
        # wait.until(EC.title_is('百度新闻——海量中文资讯平台'))
        js = 'document.documentElement.scrollTop=100000'                        #滚动条拉取最下面
        self.driver.execute_script(js)                                          #执行JS脚本
        sleep(5)


if __name__ == '__main__':
    case = TestCase()
    # case.test_case()
    case.test_case2()
