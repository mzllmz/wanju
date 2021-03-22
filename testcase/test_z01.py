#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/20 16:38
# @Author :han
# @File : test_z01.py
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
import json
import pytest
from common.log.logHandler import LogHandler
import requests
def test_01(zhongwen):
    log = LogHandler.logger
    log.info('接口名：')
    res, request1, request2 = zhongwen
    assert request2 in res.text

if __name__ == '__main__':
    pytest.main(['-s'])

