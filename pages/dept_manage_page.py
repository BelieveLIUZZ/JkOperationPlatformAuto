from base_framework.base_page import BasePage
import allure

"""
.//*[@id='admin']/div/div/div[2]/div[2]/div/div[4]/div[1]/div[3]/table/tbody/tr/td[2]
筛选查询后，通过定位部门名称的文字内容去判断和输入的条件是否一致
"""


class DeptManagePage(BasePage):

    # 元素
    # 系统设置
    # system_setting = "xpath=>.//*[@id='admin']/div/div/div[1]/ul/li[1]/div/span"
    # 部门管理
    # dept_manage = "xpath=>.//*[@id='admin']/div/div/div[1]/ul/li[1]/ul/li[3]/span"
    # 输入搜索
    # search_key = "xpath=>.//*[@id='admin']/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div[1]/div/div/input"
    # 开始查询 按钮
    # search_btn = "xpath=>.//*[@id='admin']/div/div/div[2]/div[2]/div/div[1]/div[2]"
    # 部门名称
    # dept_name = "xpath=>.//*[@id='admin']/div/div/div[2]/div[2]/div/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[2]"
    # 新增
    # new_add = "xpath=>.//*[@id='admin']/div/div/div[2]/div[2]/div/div[3]/div[2]/div"
    # 新增部门-所属区域
    # area = "xpath=>.//*[@id='admin']/div/div/div[2]/div[2]/div/div[5]/div/div[2]/form/div[1]/div/div/div/input"
    # 新增部门-所属区域-下拉选项
    # area_select = "xpath=>html/body/div[2]/div[1]/div[1]/ul/li[1]"
    # -----------------------------------------------------------------------
    system_setting = "xpath=>.//*[@id='app']/div/div/div[1]/ul/li[1]/div/span"
    dept_manage = "xpath=>.//*[@id='app']/div/div/div[1]/ul/li[2]/ul/li[2]"
    search_key = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div[1]/div/div/input"
    search_btn = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[1]/button"
    dept_name = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[2]"
    new_add = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[3]/button"
    area = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[5]/div/div[2]/form/div[1]/div/div/div/input"
    area_select = "xpath=>html/body/div[3]/div[1]/div[1]/ul/li[1]"

    def system_setting_click(self):
        self.click(self.system_setting)

    def dept_manage_click(self):
        self.click(self.dept_manage)

    # 点击输入框，并输入内容
    def search_key_input(self, text):
        self.click(self.search_key)
        return self.input_text(self.search_key, text)

    def search_btn_click(self):
        self.click(self.search_btn)

    # 部门名称 的文字   (通过名字去判断当前查询结果是否一致)
    def dept_name_text(self):
        print('部门名称---', self.get_element_text(self.dept_name))
        return self.get_element_text(self.dept_name)

    # 新增
    def new_add_click(self):
        self.click(self.new_add)
        self.click(self.area)
        self.click(self.area_select)




