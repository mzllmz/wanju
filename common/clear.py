#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/18 14:35
# @Author :han
# @File : clear.py
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
import os
import time


"""
    每三天清除一次output文件里面的内容
"""
class TimedDeleteOutput():
    t = time.time()

    def writeTime(self):
        """
        把时间写入文件
        :return:
        """
        with open("t.txt", "w", encoding='utf-8') as f:
            f.write(str(self.t))

    def removeMkdir(self,filename):
        """
        执行删除和创建文件夹来达成清空文件夹的目的
        :param filename: 要清空的文件夹名字
        :return:
        """
        time.sleep(0.01)
        os.popen(rf'rd /s/q ..\report\{filename}')  #路径
        time.sleep(0.01)
        os.popen(rf'mkdir ..\report\{filename}')

    def run(self):
        """
        判断时间是否超过三天，超过就清空文件夹
        :return:
        """
        if os.path.exists("t.txt"):
            with open("t.txt", "r", encoding='utf-8') as f:
                current = float(f.read())
                q=(self.t - current)
                t=(3*86400-q)//86400
                s=24-q//60/60
                f=60-q//60%60
                m=60-q%60%60
                print(f'剩余{int(t)}天，{int(s)}小时，{int(f)}分钟，{int(m)}秒')
                if float(self.t) - current > (3 * 86400):
                    self.removeMkdir("image")
                    self.removeMkdir("log")
                    self.removeMkdir("report")
                    # self.removeMkdir("report_html")
                    self.writeTime()
        else:
            self.writeTime()

TimedDeleteOutput().run()