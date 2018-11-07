import unittest
from base_framework.base_analyze import analyze_csv_file
from base_framework.browser_engine import BrowserEngine
from function.login_function import LoginFunction
from pages.page import Page
from nose_parameterized import parameterized
import time

login_fun = LoginFunction()
login_data = analyze_csv_file('/data/data')
print(login_data)


class TestAnalyze(unittest.TestCase):

    @classmethod
    def setUp(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        cls.page = Page(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    @parameterized.expand(login_data)  # [(adminer,123456,登录成功),(adminer,000000,密码校验错误)]
    def test_login(self, number, username, password, expect):

        self.page.login.input_username(username)
        self.page.login.input_password(password)
        result = login_fun.login_function(username, password)
        self.page.login.click_submit()
        # login_page.sleep(3)
        # alert = self.driver.switch_to_alert()
        # alert_text = alert.text
        self.page.login.get_wiondows_screen()

        # 此处应该是弹框或者根据已有的期望值与当前实际结果做对比

        try:
            self.page.login.sleep(2)
            self.assertEqual(result, expect)
        except Exception as e:
            print('Test Failed: %s' % e)
