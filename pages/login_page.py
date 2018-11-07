import allure

from base_framework.base_page import BasePage


class LoginPage(BasePage):

    # 元素
    username = "xpath=>.//*[@id='app']/div/div/div[2]/div/div[2]/div/form/div[1]/div/div/input"
    password = "xpath=>.//*[@id='app']/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/input"
    submit_btn = "xpath=>.//*[@id='app']/div/div/div[2]/div/div[2]/div/button"
    is_login = "xpath=>.//*[@id='app']/div/header/div[2]/span/div[2]/span"
    # div弹框
    msg_box = "xpath=>html/body/div[3]/p"

    # 自动登录 后续加 ini 配置文件
    def auto_login(self):
        """
            1. 读取配置文件
            2. 读取用户名和密码
            3. 获取对应元素事件
            4. 调用登录方法
        """
        pass

    # 输入用户名
    @allure.step(title='输入用户名')
    def input_username(self, text):
        self.input_text(self.username, text)

    # 输入密码
    @allure.step(title='输入密码')
    def input_password(self, text):
        self.input_text(self.password, text)

    # 登录  jenkins 持续集成时有对应的执行步骤
    @allure.step(title='点击登录')
    def click_submit(self):
        self.click(self.submit_btn)

    # 通过判断用户名 判断是否登录成功
    def is_login_success(self):
        return self.get_element_text(self.is_login)

    # 获取弹出框的文本
    def msg_box_text(self):
        print('login_page---', self.get_element_text(self.msg_box))
        return self.get_element_text(self.msg_box)


