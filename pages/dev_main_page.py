from base_framework.base_page import BasePage
import allure
import time


class DevMainPage(BasePage):
    # 系统设置
    system_setting = "xpath=>.//*[@id='app']/div/div/div[1]/ul/li[2]/div/span"
    # 部门管理
    dept_manage = "xpath=>.//*[@id='app']/div/div/div[1]/ul/li[2]/ul/li[6]/span"
    # 输入搜索  关键字
    search_key = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div[1]/div/div/input"
    # 搜索按钮
    search_btn = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[1]/button"
    # 部门元素
    dept_name = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[2]"
    # 新增  按钮
    new_add = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[3]/button"
    # 所在区域点击
    area = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[5]/div/div[2]/form/div[1]/div/div/div/input"
    # 区域选择  取第一个元素
    area_select = "class_name=>el-select-dropdown__item"
    # 所在分部
    division = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[5]/div/div[2]/form/div[2]/div/div/div/input"
    # 分部选择   取第一个元素
    division_select = "xpath=>html/body/div[2]/div[1]/div[1]/ul/li[1]"
    # 部门名称  输入
    new_dept_name = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[5]/div/div[2]/form/div[3]/div/div[1]/input"
    # 显示排序  输入
    show_order = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[5]/div/div[2]/form/div[4]/div/div[1]/input"
    # 联系电话  输入
    contact_phone = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[5]/div/div[2]/form/div[5]/div/div[1]/input"
    # 职位描述
    position_description = "xpath=>.//*[@id='app']/div/div/div[2]/div[2]/div/div[5]/div/div[2]/form/div[6]/div/div/textarea"

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
        # def new_add_click(self, deptname, showorder, contactphone, positiondescription='技术部'):
        self.click(self.new_add)
        time.sleep(3)
        self.click(self.area)
        # self.click(self.area_select)  # 取所在区域第一个元素
        # self.click(self.division)
        # time.sleep(3)
        # self.click(self.division_select)  # 去所在分部的第一个元素
        # self.click(self.new_dept_name)
        # self.input_text(self.new_dept_name, deptname)  # 部门名称
        # self.click(self.show_order)
        # self.input_text(self.show_order, showorder)  # 显示排序
        # self.click(self.contact_phone)
        # self.input_text(self.contact_phone, contactphone)  # 联系电话
        # self.click(self.position_description)
        # self.input_text(self.position_description, positiondescription)  # 描述

    def area_select_click(self):
        # time.sleep(2)
        # self.click(self.area)
        self.sleep(3)
        print('所在区域选择：', self.area_select)
        self.click(self.area_select)
