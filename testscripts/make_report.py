import os
import time
import unittest

from testscripts.test_path_config import TestPathConfig
from sys_tools.HTMLTestReportCN import HTMLTestRunner

# 设置测试保存存放的路径
report_path = os.path.dirname(os.path.abspath('.')) + '/reports/'
# 设置文件的名称，通过当前日期和时间生成测试报告名称前缀
now_time = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
# 设置报告名称   file()内置函数，python3.0，不支持file函数，可以替换成open，效果一样
report_name = report_path + now_time + 'HTMLTestTemplate.html'
report_stream = open(report_name, "wb")

# 构建suite测试套件
case_suite = unittest.TestSuite()
# case_suite.addTest(TestLogin('test_login'))
# case_suite.addTest(TestMain('test_main'))
case_suite.addTest(TestPathConfig('test_switch_search'))


if __name__ == '__main__':
    """
        stream=:开启的报告文件写入流
        verbosity=:测试执行后的打印格式(默认值为1,可选2,2显示的信息更详细,推荐使用!)
        title=:生成的报告内的标题(可选)
        description=:测试相关环境描述信息(可选)
    """
    # 初始化一个HTMLTestRunner实例对象，生成测试报告
    runner = HTMLTestRunner(stream=report_stream, title='登录逻辑测试报告文档',
                            description='测试平台：windows10       测试浏览器：Chorme        版本：68',
                            tester='测试组')
    runner.run(case_suite)
