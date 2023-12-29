# import allure
import pytest
from selenium.webdriver.common.by import By
from testcase.basecase import BaseCase


class TestPage(BaseCase):
    def __init__(self, driver):
        BaseCase.__init__(self, driver)
        driver.get('http://www.baidu.com')

# @allure.feature()
# @pytest.mark.parametrize('name',BaseCase())
    def test_page(self):
        loc = (By.ID, 'kw')
        loc2 = (By.ID, 'su')
        self.input_test('name', *loc)
        self.click(*loc2)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    test = TestPage(driver)
    # test.test_page()
    pytest.main(['-sv', 'test_pom.py'])
