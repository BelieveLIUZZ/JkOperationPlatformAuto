import configparser
import os
from selenium import webdriver

from base_framework.logger import Logger

# Create a logger instance  创建一个
logger = Logger(logger='BrowserEngine').get_log()


# class BrowserEngine(object):
class BrowserEngine:
    def __init__(self, driver):
        self.driver = driver

    """
        Read the browser type from config.ini file.  return the driver 
    """
    def open_browser(self, driver):
        # 创建实例，读取配置文件
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/configs/config.ini'
        # 父级路径
        # base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

        # 读取配置文件，直接读取ini内容
        config.read(file_path)

        browser = config.get('browserType', 'browserName')
        logger.info('You had select %s browser.' % browser)
        url = config.get('serverUrl', 'URL')
        logger.info('The test server url is: %s' % url)

        if browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info('Starting Chrome browser')
        elif browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info('Starting Firefox browser')
        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info('Starting IE browser')

        driver.maximize_window()
        logger.info('Maximize the current window')
        driver.get(url)
        logger.info('Open url:%s' % url)
        driver.implicitly_wait(30)
        logger.info('Set implicitily wait 10 seconds.')

        return driver

    def quit_browser(self):
        logger.info('Close and quit the browser. ')
        self.driver.quit()
