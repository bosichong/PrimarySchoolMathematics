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

__version__ = "0.0.1"
'''
开心Python Django 学习交流q群：217840699
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
        print(self.BASE_DIR)
        print(self.INI_PATH)
        print(os.path.isfile(self.INI_PATH))
        self.c = ConfigParser()

        self.readINI()
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
        # self.c.set('divattrs', 'divattrs', '0')  # 暂时无配置项

        self.c.set('config', 'number', '30')  # 需要生成的题数
        self.c.set('config', 'juanzishu', '5')  # 需要打印的卷子数
        self.c.set('config', 'lieshu', '3')  # 需要打印的卷子题列数
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
        div = {}  # 除法设置

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
        docx = self.c.get('config', 'docx')
        tmp_type = [add, sub, mult, div, signum, step,
                    number, is_result, is_bracket, multistep, symbols, docx, ]
        # print(tmp_type)
        return tmp_type  # 返回一个list 包含程序配置数据。

    def saveDocx(self, path):
        '''保存算数项设置数据'''
        self.c.set('config', 'docx', path)
        self.saveINI()

    def saveMultistep(self, multistep):
        '''保存算数项设置数据'''
        self.c.set('config', 'multistep', multistep)
        self.saveINI()

    def saveMultistep(self, multistep):
        '''保存算数项设置数据'''
        self.c.set('config', 'multistep', multistep)
        self.saveINI()

    def saveSymbols(self, symbols):
        '''保存运算符号设置数据'''
        self.c.set('config', 'symbols', symbols)
        self.saveINI()

    def saveInf_title(self, inf_title):
        '''保存卷子副标题设置数据'''
        self.c.set('config', 'inf_title', inf_title)
        self.saveINI()

    def saveJz_title(self, jz_title):
        '''保存卷子标题设置数据'''
        self.c.set('config', 'jz_title', jz_title)
        self.saveINI()

    def saveLieshu(self, lieshu):
        '''保存卷子题列数设置数据'''
        self.c.set('config', 'lieshu', lieshu)
        self.saveINI()

    def saveJuanzishu(self, juanzishu):
        '''保存卷子份数设置数据'''
        self.c.set('config', 'juanzishu', juanzishu)
        self.saveINI()

    def saveAdd(self, add):
        '''保存加法设置数据'''
        self.c.set('addattrs', 'carry', add)
        self.saveINI()

    def saveSub(self, sub):
        '''保存减法设置数据'''
        self.c.set('subattrs', 'abdication', sub)
        self.saveINI()

    def saveSignum(self, signum):
        '''保存题型设置数据'''
        self.c.set('config', 'signum', signum)
        self.saveINI()

    def saveStep(self, step):
        '''保存口算题步数设置数据'''
        self.c.set('config', 'step', step)
        self.saveINI()

    def saveNumber(self, number):
        '''保存口算题个数设置数据'''
        self.c.set('config', 'number', number)
        self.saveINI()

    def saveIs_Result(self, is_result):
        '''保存口算题是否求结果设置设置数据'''
        self.c.set('config', 'is_result', is_result)
        self.saveINI()

    def saveIs_Bracket(self, is_bracket):
        '''保存口算题是否使用括号设置设置数据'''
        self.c.set('config', 'is_bracket', is_bracket)
        self.saveINI()


if __name__ == '__main__':
    ac = AppConfig()

    ac.saveSignum('5')
    ac.loadINI()
