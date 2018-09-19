# encoding: utf-8
"""
@author:Administrator
@file: logger.py
@time: 2018/09/{DAY}
"""
import logging
import os
import time

# log_path 是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'logs')

# 如果不存在这个 logs 文件夹，就自动创建一个
if not os.path.exists(log_path): os.makedirs(log_path)

class Log:
    def __init__(self):
        self.logname = os.path.join(log_path,'%s.log' % time.strftime('%Y-%m-%d'))

        #第一步，创建一个logger 并设置log等级
        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.DEBUG)

        #定义handler的输入格式
        self.formatter = logging.Formatter('%(asctime)s-%(filename)s-%(lineno)d-%(levelname)s:%(message)s')

    def __console(self, level, message):

        #创建一个FileHandler,用于写于本地
        fh = logging.FileHandler(filename=self.logname, mode='a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个 StreamHandler,用于输出到控制台
        sh = logging.StreamHandler()
        sh.setFormatter(logging.DEBUG)
        sh.setFormatter(self.formatter)
        self.logger.addHandler(sh)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        #为了避免日志输出重复的问题
        self.logger.removeHandler(fh)
        self.logger.removeHandler(sh)

        #关闭打开的文件
        fh.close()
    def debug(self,message):
        self.__console('debug', message)
    def info(self,message):
        self.__console('info', message)
    def warning(self,message):
        self.__console('warning', message)
    def error(self,message):
        self.__console('error', message)

if __name__ == '__main__':
    loger = Log()
    loger.info('------测试开始-----')
    loger.warning('----出现警告----')
    loger.debug('----程序出现bug----')
    loger.error('-----程序出现error----')