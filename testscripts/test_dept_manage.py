import unittest
from base_framework.browser_engine import BrowserEngine
from pages.page import Page
from nose_parameterized import parameterized
from base_framework.base_analyze import analyze_csv_file
import configparser
import os
import time

search_data = analyze_csv_file('/data/system_dept_search_data')


class TestDeptManagement(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        self.page = Page(self.driver)

    def tearDown(self):
        pass
        # self.driver.quit()

    # 自动登录设置（正确的用户名和密码）
    def auto_login(self):

        # 创建实例，读取配置文件
        config = configparser.ConfigParser()
        # base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        # print('base_path:', base_path)
        # file_path = os.path.join(base_path + '')
        file_path = os.path.dirname(os.path.abspath('.')) + '/configs/auto_login.ini'
        config.read(file_path, encoding='utf-8')

        # 读取用户名
        username = config.get('usernames', 'username')
        print('配置用户名：', username)
        # 读取密码
        password = config.get('passwords', 'password')
        print('配置密码：', password)
        time.sleep(1)
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_submit()

    # 切换窗口、筛选查询
    @parameterized.expand(search_data)
    def test_switch_search(self, number, key_word):
        # 自动登录
        self.auto_login()
        self.page.deptmanage_page.system_setting_click()
        self.page.deptmanage_page.dept_manage_click()
        # 输入的关键字
        search_word = self.page.deptmanage_page.search_key_input(key_word)
        self.page.deptmanage_page.search_btn_click()
        result = self.page.deptmanage_page.dept_name_text()
        try:
            self.assertEqual(search_word, result)
        except Exception as e:
            print('test_switch_search  Test error: %s' % e)

    # # 新增操作
    # def test_new_add(self):
    #     self.auto_login()
    #     time.sleep(2)
    #     self.page.deptmanage_page.new_add_click()
    #
    #     time.sleep(4)




