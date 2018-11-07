import unittest
from base_framework.browser_engine import BrowserEngine
import configparser
import os
from pages.page import Page


class AutoLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        cls.driver.implicitly_wait(20)
        cls.page = Page(cls.driver)

    @classmethod
    def tearDown(cls):
        pass

    # 自动登录设置（正确的用户名和密码）
    def auto_login(self):
        # 创建实例，读取配置文件
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/configs/auto_login.ini'
        config.read(file_path, encoding='utf-8')

        # 读取用户名
        username = config.get('usernames', 'username')
        print('姓名', username)
        # 读取密码
        password = config.get('passwords', 'password')
        print("密码", password)
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_submit()

        try:
            pass
        except NameError:
            pass

