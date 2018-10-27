# encoding: utf-8
"""
@author:Administrator
@file: run_main.py
@time: 2018/09/{DAY}
"""
import os
import unittest
from common import HTMLTestRunner


def add_case(caseName='case',rule='test*.py'):

    #获取脚本所在文件夹的真是路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    case_path = os.path.join(cur_path, caseName)

    #定义discover
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern=rule)
    return discover

if __name__ == '__main__':

    curpath = os.path.realpath(os.path.dirname(__file__))
    reportpath = os.path.join(curpath, 'report', 'report.html')  # report报存的路径

    fb = open(reportpath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fb)
    runner.run(add_case())