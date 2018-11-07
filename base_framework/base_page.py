import os
import time
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base_framework.logger import Logger


# Create a logger instance 创建一个logger的实例
logger = Logger(logger='BasePage').get_log()


# class BasePage(object):
class BasePage:
    """
        封装一个页面基类，让所有页面都继承这个基类，此基类封装一些页面操作的常用方法方便调用。
    """
    def __init__(self, driver):
        """
        :param driver:
        """
        self.driver = driver

    """
        退出浏览器
    """
    def quit_browser(self):
        self.driver.quit()

    """
        浏览器前进一步操作
    """
    def forward_browser(self):
        self.driver.forward()
        logger.info('前进：Click forward on current page')

    """
        浏览器后退一步操作
    """
    def back_browser(self):
        self.driver.back()
        logger.info('后退：Click back on current page')

    """
        隐式等待  :param sencond:
    """
    def implicit_wait(self, senconds):
        self.driver.implicitly_wait(senconds)
        logger.info('等待：wait for %s senconds' % senconds)

    """
        点击关闭当前窗口
    """
    def close_current_window(self):
        try:
            self.driver.close()
            logger.info('关闭当前窗口：Close and quit current window')
        except NameError as e:
            print(e)
            logger.error('关闭窗口出错：Failed to quit the window with %s' % e)

    """
        刷新操作
    """
    def refresh(self):
        try:
            self.driver.refresh()
            logger.info('刷新：Refresh the browser')
        except NameError as e:
            print(e)
            logger.error('刷新失败：Failed to refresh the browser with %s' % e)

    """
        截取屏幕操作
    """
    def get_wiondows_screen(self):
        """
            将截图保存在项目根目录的指定文件夹/screenshots/目录下
        """
        # 获取路径中的目录名
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        # 取到当前时间并格式化
        time_format = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name_path = file_path + time_format + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name_path)
            logger.info('截图：Had take a screenshot and save to folder：/screenshots/')
        except NameError as e:
            print(e)
            logger.error('截图失败：Failed to take a screenshot! %s' % e)
            self.get_wiondows_screen()

    """
        元素定位：封装了8中元素定位的方式，针对元素做了异常处理操作并记录日志
    """
    def find_element(self, selector):
        """
            元素定位，通过 => 切割字符串，可以参照页面里元素定位的方法
            submit_btn = 'id => su'
            link_text = 'xpath =>.//*[@id='u1']/a[7]' 百度首页登录链接定位
            如果使用 = 等切割，很多xpath定位中包含 = 等号，造成切割不准确，影响元素定位
            :param selector:
            :return: element
        """
        element = ''

        # 默认如果不使用定义好的定位方式，采取默认使用id定位元素
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        # 以'=>'作为分隔符(返回一个列表)，取[n]第几片
        selector_way = selector.split('=>')[0]  # 定位方式
        selector_value = selector.split('=>')[1]  # 值

        if selector_way == 'i' or selector_way == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element [ %s ] successful "
                            "by %s via value: %s " % (element.text, selector_way, selector_value))
            except NoSuchElementException as e:
                print('定位元素:', e)
                logger.error('NoSuchElementException:%s' % e)
                self.get_wiondows_screen()
        elif selector_way == 'n' or selector_way == 'name':
            element = self.driver.find_element_by_name(selector_value)

        elif selector_way == 'c' or selector_value == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)

        elif selector_way == 'l' or selector_way == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)

        elif selector_way == 'p' or selector_way == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)

        elif selector_way == 't' or selector_way == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)

        elif selector_way == 'x' or selector_way == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element [ %s ] successful "
                            "by %s via value: %s " % (element.text, selector_way, selector_value))
            except NoSuchElementException as e:
                print('xpath定位失败:', e)
                logger.error('NoSuchElementException:%s' % e)
                self.get_wiondows_screen()
        elif selector_way == 's' or selector_way == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)

        else:
            raise NameError('Please enter a valid type of targeting elements.')

        return WebDriverWait(self.driver, 20, 0.2).until(ec.visibility_of(element))
        # return WebDriverWait(self.driver, 20, 0.2).until(ec.presence_of_element_located(element))

    """
        对元素进行输入操作
    """
    def input_text(self, selector, text):
        element = self.find_element(selector)
        element.clear()
        try:
            element.send_keys(text)
            logger.info('输入内容：Had type [ %s ] in inputBox' % text)
        except NameError as e:
            print('输入错误：', e)
            logger.error('输入错误：Failed to type in input text with %s' % e)
            self.get_wiondows_screen()

    """
        清除文本框操作
    """
    def clear(self, selector):
        element = self.find_element(selector)
        try:
            element.clear()
            logger.info("清除：Clear text in input box before typing.")
        except NameError as e:
            logger.error("清除失败：Failed to clear in input text with %s" % e)
            self.get_wiondows_screen()

    """
        点击元素
    """
    def click(self, selector):
        element = self.find_element(selector)
        try:
            element = WebDriverWait(self.driver, 30).until(ec.visibility_of(element))
            element.click()
        except NameError as e:
            print('点击失败：', e)
            logger.error("点击失败：Failed to click the element with %s" % e)

    """
        获取网页标题
    """
    def get_page_title(self):
        logger.info("当前网页标题：Current page title is %s" % self.driver.title)
        return self.driver.title

    """
        获取元素文本
    """
    def get_element_text(self, selector):
        element = self.find_element(selector)
        try:
            return element.text
        except NameError as e:
            logger.error("获取元素失败：Failed to get text" % e)

    """
        跳转frame；切换窗口
    """
    def switch_iframe_to(self, frame='myiframe'):
        try:
            self.driver.switch_to.frame(frame)
        except NameError as e:
            logger.info('切换frame：iframe is switched or', format(e))

    """
        下拉框：先定位下拉框，再定位下拉框里面的值
    """
    def select_down_box(self, selector, way, value):
        """
        :param selector: 定位元素
        :param way: 定位类型；选项<索引、value值、文本值>
        :param value: 内容；选项值
        :return:
        """
        element = self.find_element(selector)
        if way == 'index' or way == 'i':
            try:
                Select(element).select_by_index(value)  # 通过index索引定位
                logger.info('索引定位：Has selected\' %s \' .' % value)
            except NameError as e:
                logger.error("索引定位失败：Failed to select the element with %s" % e)
        elif way == 'value' or way == 't':
            try:
                Select(element).select_by_value(value)
                logger.info('value定位：Has selected\' %s \' .' % value)
            except NameError as e:
                logger.error("value定位失败：Failed to select the element with %s" % e)
        elif way == 'visible_text' or way == 'vt':
            try:
                Select(element).select_by_visible_text(value)
                logger.info('visible_text定位：Has selected\' %s \' .' % value)
            except NameError as e:
                logger.error("visible_text定位失败：Failed to select the element with %s" % e)
        else:
            raise NameError("Please enter a valid type of targeting type.")

    """
        等待
    """
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
