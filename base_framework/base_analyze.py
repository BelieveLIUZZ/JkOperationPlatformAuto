import csv
import json
import os
import xlrd

"""
    封装xlsx 写入 csv 的方法
    封装解析数据的方式：CSV、txt、Json
"""
from base_framework.base_path_config import BASE_PATH


def xlsx_to_csv(xlsx_path, sheet_name, csv_path):
    """
    :param xlsx_path: 读取xlsx文件
    :param sheet_name: sheet 的名称
    :param csv_path: 写入的CSV文件路径
    :return:
    """
    old_file_path = BASE_PATH + csv_path
    try:
        os.remove(old_file_path)
    except Exception as msg:
        print('跳过：', msg)


def analyze_csv_file(file_name):
    """
        :param file_name: 文件名称
        :return: 返回一个列表
    """

    print('解析base_path:', BASE_PATH)
    path = BASE_PATH + file_name + '.csv'
    with open(path, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        # 声明一个空列表
        data_list = []
        for item in data:
            data_list.append(tuple(item))
            print(item)
        return data_list


# 读取json 数据
def analyze_json_file(file_name, key):
    path = '../data/' + file_name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)
        # 根据键名key取出大列表
        source_list = data[key]
        return source_list


def analyze_txt_file(file_name):
    """
        readlines():读取多行数据
        readline():读取单行数据
        read():读取数据,获取大量内容的文件时,一般需要制定文件大小.
        :param file_name:
    """
    path = '../data/' + file_name + '.txt'
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()
        data_list = []
        for item in data:
            """
                strip():去除换行符，制表符，空格
                split():以','作为分隔符，返回列表的形式的数据集合
            """
            print(item.strip().split(','))
            data_list.append(item.strip().split(','))
        return data_list
