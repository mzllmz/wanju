#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/21 16:19
# @Author :han
# @File : yamlDATA.py
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

import yaml
# 读
def readYaml():
    with open('../data/key.yml',"r",encoding="utf-8") as f:
        # d = yaml.load(f,Loader=yaml.FullLoader)
        d = yaml.safe_load(f)
        data= list(zip(d['key'],d['chars']))
        return data

# 写
def writeYaml(path,content):
    with open(path,"w",encoding="utf-8") as f:
        yaml.dump(content,f)

# d='qwerzx';c='asdfg'
# data= list(zip(d,c))
# print(data)