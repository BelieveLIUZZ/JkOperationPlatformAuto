import unittest
from nose_parameterized import parameterized
from base_framework.base_analyze import analyze_csv_file
from pages.page import Page
from base_framework.browser_engine import BrowserEngine
import time


key_data = analyze_csv_file('/data/baidu_search')


class TestBaidu(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        self.page = Page(self.driver)

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(key_data)
    def test_baidu_search(self, number, key_word):
        self.page.baidu_page.input_keyword(key_word)
        time.sleep(3)
        self.page.baidu_page.click_search_btn()
        time.sleep(6)




