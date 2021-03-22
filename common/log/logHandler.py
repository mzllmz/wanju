# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 15:23
# @Author : fanfan
# @File : logHandler.py
# @Project : kaoYanBang
import logging
import time


class time0():
    def time1(self):
        # 时间戳 路径当中不要有冒号
        __t = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()).split("-")
        __t2 = __t[2].split(" ")
        __s = f"{__t[0]}年{__t[1]}月{__t2[0]}日{__t2[1]}时{__t[3]}分{__t[4]}秒"
        __logname = f"{__t[0]}年{__t[1]}月{__t2[0]}日"


class LogHandler():
    # 日志存放路径
    fileLogPath = f'../report/{time0().time1()}.log'
    # 设置日志收集器
    logger = logging.getLogger(__name__)
    # 设置等级
    logger.setLevel(level=logging.INFO)
    # 设置文件处理器
    __fhandler = logging.FileHandler(filename=fileLogPath, encoding="utf-8")
    # 设置控制台处理器
    __shandler = logging.StreamHandler()
    # 设置格式化
    # __format = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    __format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    # 设置文件处理器格式化
    __fhandler.setFormatter(__format)
    # 设置控制台处理器格式化
    __shandler.setFormatter(__format)
    # 添加处理器
    logger.addHandler(__fhandler)
    logger.addHandler(__shandler)
