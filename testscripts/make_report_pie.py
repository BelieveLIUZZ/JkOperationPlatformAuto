import os
import time
import unittest
from sys_tools.HTMLTestReportCN import HTMLTestRunner


def create_suite():
    case_suite = unittest.TestSuite()  # 测试集
    report_path = os.path.dirname(os.getcwd()) + '\\testscripts\\'

    discover = unittest.defaultTestLoader.discover(
        start_dir=report_path,
        pattern='test_*.py',
        top_level_dir=None
    )

    for test_case in discover:
        case_suite.addTests(test_case)
        print(test_case)
    return case_suite


def report():
    # # 设置测试保存存放的路径
    # report_path = os.path.dirname(os.path.abspath('.')) + '/reports/'
    # # 设置文件的名称，通过当前日期和时间生成测试报告名称前缀
    # now_time = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    # # 设置报告名称   file()内置函数，python3.0，不支持file函数，可以替换成open，效果一样
    # report_name = report_path + now_time + 'HTMLTestTemplate.html'

    report_name = os.path.dirname(os.path.abspath('.')) + '/reports/result.html'

    return report_name


if __name__ == '__main__':
    TestSuite = create_suite()
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(
        verbosity=2,
        stream=fp,
        title='测试报告',
        description='测试用例执行情况',
        # tester='测试组人员'
    )
    Runner.run(TestSuite)
    fp.close()
