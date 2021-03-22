#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/20 16:13
# @Author :han
# @File : conftest.py
# @Project : pydata
# ctrl + d  ctrl + y
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
'''
接口自动化：
    本质：url   测试就是对 

'''

import pytest
import requests  # 爬虫
import json
#把字典转换为json字符串
# a={'name':123}
# a=json.dumps(a)
# print(type(a))
# #将字典形式的字符串转换为字典
# b=json.loads(a)
# print(b['name'])
from data.yamlDATA import readYaml
from common.log.logHandler import LogHandler

# @pytest.fixture(params=[['1775e2db4cae63cecffa0266ef3f17c9','韩'],
#                 ['1775e2db4cae63cecffa0266ef3f17c9','富'],
#                 ['1775e2db4cae63cecffa0266ef3f17c9','富']])

log=LogHandler.logger
# get请求
@pytest.fixture(params=readYaml())
def zhongwen(request):
    url = 'http://v.juhe.cn/cccn/to_telecodes.php'
    # get请求   1. 直接跟在url后面   2.把参数赋值给一个变量，请求时传递给params
    para = f'key={request.param[0]}&chars={request.param[1]}'
    log.info(f'请求{request.param[0]}成功,得到{request.param[1]}成功')
    res = requests.get(url, params=para)  #参数传递给params
    return res,request.param[0], request.param[1]


def jiami(x):
    return '20'+oct(int(str(x)[2:])*1000)[2:]
# post请求
@pytest.fixture()
def pp():
    url = 'http://v.juhe.cn/cccn/to_telecodes.php'
    head = {'Content=Type': 'application/json'}
    para = {'name': '博文', 'no': jiami(201101)}
    para = json.dumps(para).encode('utf-8')
    #接收响应数据：所有的数据（请求的url，head，body）
    #接收相应实体的方式：1. text 结果是个字符串
    #                2. content 结果是字节码
    #                3. 仅限于响应数据是json格式时，将响应数据格式更改为字典
    res = requests.post(url,headers=head,data=para).json()   #参数给headers，请求实体传给字典

    return res