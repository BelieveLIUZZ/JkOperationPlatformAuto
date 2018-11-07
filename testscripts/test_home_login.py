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


class TestHomeLogin(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        self.page = Page(self.driver)

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(login_data)
    def test_home_login(self, number, username, password, expect):

        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_submit()
        self.page.login.get_wiondows_screen()

        result = login_fun.login_function(username, password)
        # 此处应该是弹框或者根据已有的期望值与当前实际结果做对比
        # （登录后的弹框，是前端通过数据渲染出来的，持续3秒，定位元素这块目前定位不到）
        # result = self.page.login.msg_box_text()
        # print('div弹框文字', result)

        try:
            self.page.login.sleep(2)
            self.assertEqual(result, expect)

        except Exception as e:
            print('Test Failed: %s' % e)
