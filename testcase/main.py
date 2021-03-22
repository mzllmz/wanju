#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/21 17:21
# @Author :han
# @File : main.py
# @Project : pydata
#ctrl + d  ctrl + y
"""
多行注释
"""
'''
由数字，字母，下划线
不能数字开头
不能内置关键字
严格区分大小写
'''
"""
alt+ctrl+l  排版
"""
import pytest
import os
from common.clear import TimedDeleteOutput as tt

tt().run()

if __name__ == '__main__':

    pytest.main(["-sv",
                 r"D:\jiekou\testcase\test_z01.py",
                 rf"--alluredir=D:\jiekou\report\aull",
                 "--clean-alluredir"])

    os.popen(rf"allure generate D:\jiekou\report\aull  -o  jiekou\report\aull_html  --clean") #生成allure报告
