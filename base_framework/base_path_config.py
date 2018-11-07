"""
    公共文件路径的配置
"""
import os

"""
    通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。
    如果结构不同，可自行修改。os.path.join()，不要直接+'\\xxx\\ss'这样
    用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和
"""
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print('基本路径', BASE_PATH)
DATA_PATH = os.path.join(BASE_PATH, 'data')
CONFIGS_PATH = os.path.join(BASE_PATH, 'configs')
REPORTS_PATH = os.path.join(BASE_PATH, 'reports')



