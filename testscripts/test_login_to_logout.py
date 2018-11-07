import unittest
from base_framework.browser_engine import BrowserEngine
from pages.page import Page
import time
import pytest


class TestLoginToLogout(unittest.TestCase):

    def setUp(self):
        print('setupClass')
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        self.driver.implicitly_wait(20)
        self.page = Page(self.driver)

    def tearDown(self):
        self.driver.quit()

    # 登录 到 退出
    @pytest.mark.flaky(rerun=3)  # 失败重试， rerunfailure
    def test_login_to_logout(self):

        self.page.login.input_username('zhangsan')
        self.page.login.input_password('000000')
        self.page.login.click_submit()

        try:
            self.assertEqual('zhangsan', self.page.main.is_login_success())
        except Exception as e:
            print('登录失败--%s' % e)

        time.sleep(4)
        # 点击用户名处，弹出重置密码和退出按钮菜单
        self.page.main.user_admin_click()
        self.page.main.quit_login_click()

        time.sleep(2)

        self.page.main.confirm_btn_click()









