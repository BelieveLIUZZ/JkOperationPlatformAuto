import logging
import os
import time


# class Logger(object):
class Logger:
    """
        指定保存日志的文件路径，日志级别，以及调用文件；将日志存入指定的文件目录中
    """
    def __init__(self, logger):
        # 返回一个具有指定名称的日志程序，如果需要，则创建它;如果没有指定名称，则返回根日志记录器。
        self.logger = logging.getLogger(logger)
        # 设置日志等级  DEBUG < INFO < WARNING < ERROR < CRITICAL
        self.logger.setLevel(logging.DEBUG)

        # 格式化 log 日志文件名
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        print('日志路径：', log_path)
        path_format = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
        log_name = log_path + path_format + '.log'
        # 创建一个Handler，用于写入日志文件，指定编码格式，不然会有乱码
        file_handler = logging.FileHandler(log_name, encoding='UTF-8')
        file_handler.setLevel(logging.DEBUG)

        # 创建一个Handler，用于输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # 定义Handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # 给logger添加Handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def get_log(self):
        return self.logger


"""
logging日志模块四大组
日志器	Logger	提供了应用程序可一直使用的接口
处理器	Handler	将logger创建的日志记录发送到合适的目的输出
过滤器	Filter	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器	Formatter	决定日志记录的最终输出格式

日志器（logger）是入口，真正干活儿的是处理器（handler），
处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。
"""


