from base_framework.base_page import BasePage


class BaiduPage(BasePage):

    # 元素
    # 输入框
    input_textview = "id=>kw"
    # 搜索按钮
    search_button = "xpath=>.//*[@id='su']"

    # 操作
    def input_keyword(self, text):
        self.sleep(3)
        self.input_text(self.input_textview, text)

    def click_search_btn(self):
        self.click(self.search_button)



