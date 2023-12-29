from selenium import webdriver


class BaseCase(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *loa):
        return self.driver.find_element(*loa)

    def input_test(self, text, *loa):
        self.get_element(*loa).send_keys(text)

    def click(self, *loa):
        self.get_element(*loa).click()
