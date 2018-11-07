from base_framework.base_page import BasePage


class MainPage(BasePage):

    # 通过登录名判断是否登录成功
    login_name = "xpath=>.//*[@id='app']/div/header/div[2]/span/div[2]/span"
    # 信息管理
    information_manage = "xpath=>.//*[@id='app']/div/div/div[1]/ul/li[2]/ul/li[1]/span"
    # 信息管理-健康资讯
    health_information = "xpath=>.//*[@id='app']/div/div/div[1]/ul/li[2]/ul/li[1]/span"
    # 用户名 user adminer
    user_adminer = "xpath=>.//*[@id='app']/div/header/div[2]/span/div/span"
    # 退出系统按钮
    quit_login = "selector_selector=>.el-button.el-button--danger.el-button--mini.is-plain"
    # 弹出框的确认按钮
    confirm_btn = "xpath=>/html/body/div[3]/div/div[3]/button[2]"

    login_name = "xpath=>.//*[@id='app']/div/header/div[2]/span/div[2]/span"
    information_manage = "xpath=>.//*[@id='app']/div/div/div[1]/ul/li[2]/div/span"

    """
        如果用例执行从登录开始，可以通过自动登录
        自动登录 后续加 ini 配置文件
    """
    def auto_login(self):
        """
            1. 读取配置文件
            2. 读取用户名和密码
            3. 获取对应元素事件
            4. 调用登录方法
        """
        pass

    # 通过登录人名字， 判断是否登录成功
    def is_login_success(self):
        return self.get_element_text(self.login_name)

    def info_manage(self):
        self.click(self.information_manage)

    def health_info(self):
        self.click(self.health_information)

    # 点击用户名处，弹出下拉菜单
    def user_admin_click(self):
        self.click(self.user_adminer)

    # 退出按钮
    def quit_login_click(self):
        self.click(self.quit_login)

    # 点击 弹出退出框的确认按钮
    def confirm_btn_click(self):
        self.click(self.confirm_btn)


