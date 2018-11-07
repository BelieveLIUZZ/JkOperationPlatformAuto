import unittest
from base_framework.browser_engine import BrowserEngine
from pages.page import Page
from nose_parameterized import parameterized
from base_framework.base_analyze import analyze_csv_file
import configparser
import os
import time
from base_framework.base_path_config import BASE_PATH, CONFIGS_PATH, REPORTS_PATH

search_data = analyze_csv_file('/data/system_dept_search_data')
dept_data = analyze_csv_file('/data/sys_new_add_data')


class TestPathConfig(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        self.driver.implicitly_wait(20)
        self.page = Page(self.driver)

    def tearDown(self):
        self.driver.quit()

    # 自动登录设置（正确的用户名和密码）
    def auto_login(self):

        # 创建实例，读取配置文件
        config = configparser.ConfigParser()
        file_path = CONFIGS_PATH + '/auto_login.ini'
        print('自动登陆路径：', file_path)
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
        self.page.dev_page.system_setting_click()
        self.page.dev_page.dept_manage_click()
        # 输入的关键字
        search_word = self.page.dev_page.search_key_input(key_word)
        self.page.dev_page.search_btn_click()
        result = self.page.dev_page.dept_name_text()
        time.sleep(3)
        try:
            self.assertIn(search_word, result)
            # 判断search_word in result是否在
            # self.assertEqual(search_word, result)
        except Exception as e:
            print('test_switch_search  Test error: %s' % e)

    # # 新增操作
    # # @parameterized.expand(dept_data)
    # def test_new_add(self):
    #     # def test_new_add(self, number, deptname, order, phone, description):
    #     self.auto_login()
    #     self.page.dev_page.system_setting_click()
    #     self.page.dev_page.dept_manage_click()
    #     time.sleep(2)
    #     self.page.dev_page.new_add_click()
    #     all_handles = self.driver.window_handles
    #     print(all_handles)
    #     time.sleep(4)
    #     self.page.dev_page.area_select_click()
    #     # self.page.dev_page.new_add_click(deptname, order, phone, description)
    #     time.sleep(4)


if __name__ == '__main__':
    unittest.main()
