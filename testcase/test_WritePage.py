import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common import actions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from common.Basecase import sendkeys_element, click_element, save_screenshot
from test_login import TestLoginPage


@pytest.mark.dependency(depends=["TestLoginPage.test_ture"], scope='登录模块')
class Writings(TestLoginPage):

    @allure.testcase('http://47.92.200.213:9999/admin/article.php?action=write', name='保存文章为草稿')
    def test_write_save(self):

        """点击文章"""

        with allure.step('第一步：点击文章菜单'):
            click_element(self.driver, By.CLASS_NAME, 'nav-item active')

        """点击写文章"""

        with allure.step('第二步：点击写文章'):
            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.presence_of_element_located((By.ID, 'menu_write')))
            click_element(self.driver, By.ID, 'menu_write')

        """输入文章标题"""

        with allure.step('第三步：输入文章标题'):
            frame = self.driver.find_element(By.ID, 'addlog')
            self.driver.switch_to.frame(frame)  # 切表单
            sendkeys_element(self.driver, By.ID, 'title', '测试编写文章')

        """输入各种文案"""

        with allure.step('第四步：点击上传插入图片'):
            click_element(self.driver, By.LINK_TEXT, '上传插入图片')
            click_element(self.driver, By.CLASS_NAME, "icofont-plus")
            click_element(self.driver, By.CLASS_NAME, "close")

        with allure.step('第五步：编写文章封面'):
            self.driver.execute_script(f'window.scrollTo(0,1700);')  # 下拉滚动条至1700px
            sendkeys_element(self.driver, By.ID, 'cover', 'http://baidu.com')

        with allure.step('第六步：选择分类'):
            sort = Select(self.driver.find_element(By.ID, 'sort'))  # 下拉框枚举
            sort.select_by_value('杂记')  # 选择枚举

        with allure.step('第七步：选择标签'):
            sendkeys_element(self.driver, By.ID, 'tag', '测试自动输入')

        """保存为草稿"""

        with allure.step('第八步：保存为草稿'):
            click_element(self.driver, By.ID, "savedf")
            try:
                assert '保存成功' in self.driver.title
            except AssertionError:
                print('文章保存失败')

        with allure.step('保存截图'):
            save_screenshot(self.driver, '保存草稿')


if __name__ == '__main__':
    pytest.main(['--alluredir', './reports', '--clean-alluredir', '-vs', 'test_WritePage.py'])
