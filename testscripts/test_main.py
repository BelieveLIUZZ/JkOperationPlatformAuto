import unittest
from base_framework.browser_engine import BrowserEngine
from pages.page import Page
import time


class TestMain(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        self.driver.implicitly_wait(10)
        self.page = Page(self.driver)

    def tearDown(self):
        # self.driver.quit()
        print('tearSown----')
        pass

    def test_main(self):
        self.page.login.input_username('zhangsan')
        self.page.login.input_password('000000')
        self.page.login.click_submit()
        time.sleep(2)

        # try:
        #     self.assertEqual('adminer', self.page.login.is_login_success())
        #     # assert 'admin' == login_page.is_login_success()
        # except NameError as e:
        #     print('Test Failed: %s' % e)

        self.page.dev_page.system_setting_click()  # 系统设置
        self.page.dev_page.dept_manage_click()  # 部门管理
        self.page.dev_page.new_add_click()  # 新增
        self.page.dev_page.area_select_click()  # 所在区域选择


if __name__ == '__main__':
    unittest.main()
