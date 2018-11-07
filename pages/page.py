from pages.dev_main_page import DevMainPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.dept_manage_page import DeptManagePage
from pages.baidu_page import BaiduPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def main(self):
        return MainPage(self.driver)

    @property
    def deptmanage_page(self):
        return DeptManagePage(self.driver)

    @property
    def dev_page(self):
        return DevMainPage(self.driver)

    @property
    def baidu_page(self):
        return BaiduPage(self.driver)
