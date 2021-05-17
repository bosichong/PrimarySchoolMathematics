#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-11-02
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.2vv.net
# @Title   : 基于Python开发的小学生口算题生成器
# @Url     : http://2vv.net/blog/83.html
# @Details : Python实现小学生加减乘除速算考试题卷。
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            vscode


import os
from configparser import ConfigParser

__version__ = "0.1.0"
'''
开心Python Flask Django 学习交流q群：217840699
Author  : J.sky
Mail    : bosichong@qq.com
'''


class AppConfig:
    '''
    APP配置文件，将一些程序配置数据保存的ini文件里。
    '''

    # ini程序所在目录，也是当前程序的根目录
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # INI文件地址
    INI_PATH = os.path.join(BASE_DIR, 'config.ini')
    # DOCX 默认的目录地址，存放在项目目录根目录docx/
    DOCX = BASE_DIR

    def __init__(self):
        # print(self.BASE_DIR)
        # print(self.INI_PATH)
        # print(os.path.isfile(self.INI_PATH))
        self.c = ConfigParser()

        # 若没有配置文件，则创建。
        self.isINI()

        self.readINI()

    def isINI(self):
        # 若没有配置文件，则创建。
        if(not os.path.isfile(self.INI_PATH)):
            # print("ini文件不存在，开始创建！")
            self.create_ini()


    def create_ini(self):
        '''
        创建INI文件及默认数据
        :return
        '''
        # 创建section及选项
        self.c.add_section('config')

        self.c.set('config', 'docx', self.DOCX)  # 设置文件默认保存目录

        self.c.set('config', 'signum', '1')  # 包含题型需要的 1+ 2- 3* 4/
        self.c.set('config', 'step', '1')  # 生成几步运算, 默认: 1 取值范围 1-3
        self.c.set('config', 'is_result', '0')  # int 0求结果，1求运算项
        self.c.set('config', 'is_bracket', '0')  # int 是否需要括号 0不需要 1需要

        # 包括 四个运算项及结果数值范围设置。
        self.c.set('config', 'multistep', '[[1,9],[1,9],[1,9],[1,9],[1,9]]')
        # 包括 四个运算项及结果数值范围设置。
        self.c.set('config', 'symbols',
                   '[[1, 0, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0]]')

        self.c.add_section('addattrs')
        self.c.set('addattrs', 'carry', '1')  # 进位随机选择项单选，随机1，进位2，不进位3
        self.c.add_section('subattrs')
        self.c.set('subattrs', 'abdication', '1')  # 退位随机选择项单选，随机1，退位2，不退位3
        # self.c.set('multattrs', 'multattrs', '0')  # 暂时无配置项
        self.c.add_section('divattrs')
        self.c.set('divattrs', 'remainder', '2')  # 除法 随机1，整除2，有余数3

        self.c.set('config', 'number', '30')  # 需要生成的题数
        self.c.set('config', 'juanzishu', '3')  # 需要打印的卷子数
        self.c.set('config', 'lieshu', '4')  # 需要打印的卷子题列数
        self.c.set('config', 'jz_title', '小学生口算题')  # 需要打印的卷子题列数
        self.c.set('config', 'inf_title',
                   '姓名：__________ 日期：____月____日 时间：________ 对题：____道')  # 需要打印的卷子题列数

        self.saveINI()  # 创建INI文件

    def readINI(self):
        """ ini文件读取，返回一个INI配置对象
         或是用来更新内存中的配置文件数据
         """

        self.c.read(self.INI_PATH, encoding='utf-8')

    def saveINI(self):
        '''保存或是更新ini文件'''
        with open(self.INI_PATH, mode='w', encoding='utf-8') as ini:
            self.c.write(ini)

    def loadINI(self):
        '''读取并返回配置数据'''
        self.readINI()  # 更新内存中配置文件的数据
        add = {"carry": int(self.c.get('addattrs', 'carry')), }
        sub = {"abdication":  int(self.c.get('subattrs', 'abdication')), }
        mult = {}  # 乘法设置
        div = {"remainder":  int(self.c.get(
            'divattrs', 'remainder')), }  # 除法设置

        signum = int(self.c.get('config', 'signum'))
        step = int(self.c.get('config', 'step'))
        number = int(self.c.get('config', 'number'))
        is_result = int(self.c.get('config', 'is_result'))
        is_bracket = int(self.c.get('config', 'is_bracket'))

        multistep = eval(self.c.get('config', 'multistep'))
        tmpsym = eval(self.c.get('config', 'symbols'))
        symbols = [[], [], []]
        kk = 0
        for x in tmpsym:
            for y in x:
                if y > 0:
                    symbols[kk].append(y)
            kk += 1

        juanzishu = int(self.c.get("config", "juanzishu"))
        lieshu = int(self.c.get("config", "lieshu"))
        jz_title = self.c.get("config", "jz_title")
        inf_title = self.c.get("config", "inf_title")
        docx = self.c.get('config', 'docx')
        tempconfig = {"add": add, "sub": sub, "mult": mult, "div": div, "signum": signum, "step": step, "number": number,
                      "is_result": is_result, "is_bracket": is_bracket, "multistep": multistep, "symbols": symbols,
                      "juanzishu": juanzishu, "lieshu": lieshu, "jz_title": jz_title, "inf_title": inf_title, "docx": docx,
                      }
        # print(tmp_type)
        return tempconfig  # 返回一个字典 包含程序配置数据。

    def saveAll(self,data):
        '''
        保存所有配置文件数据到INI
        
        '''
        # 分解数据，用来保存INI
        l1 = data[0][-1]
        l2 = data[1]
        self.c.set('config', 'docx', l2["docx"])
        self.c.set('config', 'signum', str(l1["signum"]))
        self.c.set('config', 'step', str(l1["step"]))
        self.c.set('config', 'is_result', str(l1["is_result"]))
        self.c.set('config', 'is_bracket', str(l1["is_bracket"]))
        self.c.set('config', 'multistep', str(l1["multistep"]))
        self.c.set('config', 'symbols', str(l1["symbols"]))
        self.c.set('config', 'number', str(l1["number"]))
        self.c.set('config', 'juanzishu', str(l2["juanzishu"]))
        self.c.set('config', 'lieshu', str(l2["lieshu"]))
        self.c.set('config', 'jz_title', l2["jz_title"])
        self.c.set('config', 'inf_title', l2["inf_title"])
        self.c.set('addattrs', 'carry', str(l1["add"]["carry"]))
        self.c.set('subattrs', 'abdication', str(l1["sub"]["abdication"]))
        self.c.set('divattrs', 'remainder', str(l1["div"]["remainder"]))
        self.saveINI()#保存所有配置项




if __name__ == '__main__':
    ac = AppConfig()

    ac.saveSignum('5')
    ac.loadINI()
