#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-11-02
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 基于Python开发的小学生口算题生成器
# @Url     : http://www.17python.com/blog/29
# @Details : Python实现小学生加减乘除速算考试题卷。
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm


'''
孩子上小学一年级了，加减乘除的口算就要开始练习了，估计老题肯定会让家长出题，所以提前准备一下.

利用Python开发了一套自动生成小学生口算题的小应用。而且今天是程序员节，撸200行代码庆祝一下。：）

程序核心功能：

    1.根据条件生成相关的口算题.

    2.提供一个程序界面供用户设置相关参数

    3.保存为.docx用来打印.


开心Python Django 学习交流q群：217840699


Author  : J.sky
Mail    : bosichong@qq.com

Author  : rcddup
Mail    : 410093793@qq.com

Author  : andywu1998
Mail    : 1078539713@qq.com

'''

import random
import re

from utils.PSM_help import *

__version__ = "0.2.0"


class Generator(object):
    '''
    口算题生器核心类，负责生成完整的口算题
    '''
    #######加减乘除相关设置#####
    addattrs = None
    subattrs = None
    multattrs = None
    divattrs = None
    #####算式种类及算式题个数设置
    signum = None
    step = None
    is_result = None
    is_bracket = None
    number = None
    ########多步算式题选项设置######
    multistep = None
    symbols = None
    data_list = None  # 生成的口算题

    def __init__(self, addattrs, subattrs, multattrs, divattrs, signum, step, number, is_result, is_bracket, multistep,
                 symbols):
        '''
        :param addattrs: dict 加法设置属性，
       进位随机选择项单选，随机1，进位2，不进位3
        {"carry":1,}

        :param subattrs: dict 减法设置属性，
        退位随机选择项单选，随机1，退位2，不退位3
        {"abdication":1,}

        :param:multattrs dict 乘法
        数值范围设置
        {"result":[21,81],}

        :param:divattrs dict 除法
        数值范围设置
        {"result":[1,9],}


        :param signum: list 包含题型需要的 1+ 2- 3* 4/
        :param step: int 生成几步运算, 默认: 1 取值范围 1-3
        :param is_result :int 0求结果，1求运算项
        :param is_bracket: int 是否需要括号 0不需要 1需要
        :param num: int 需要生成的题数


        :param multistep =None: list 运算项及结果范围设置属性，
        包括 四个运算项及结果数值范围设置，
        [[1,9],[1,9],[1,9],[1,9],[10,20],]

        :param symbols list
        symbols: list 默认包括三组list,分别代表2或3步算式需要题型种类+-*/
        2+3-5  symbols = [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+


        '''

        if step is None:
            raise Exception("required param signum is missing or signum is None")
        if step not in (1, 2, 3):
            raise Exception("param signum must be 1 or 2 or 3")

        self.addattrs = addattrs
        self.subattrs = subattrs
        self.multattrs = multattrs
        self.divattrs = divattrs

        self.signum = signum
        self.step = step
        self.is_result = is_result
        self.is_bracket = is_bracket
        self.number = number

        self.multistep = multistep

        self.symbols = symbols

        self.__data_list = []  # 生成的口算题

    def __getFormula(self):
        '''根据给出的属性返回一道合法的口算题'''

        f = []
        for i in range(self.step+1):
            f.append(self.multistep[i])
        if self.step == 1:
            # 返回一步口算题

            return getOne(f, self.signum, self.multistep[4], self.addattrs["carry"],
                          self.subattrs["abdication"], self.is_result)
        elif self.step >1:
            return getMoreStep(f, self.multistep[4], self.symbols,self.step, self.addattrs["carry"],
                          self.subattrs["abdication"],self.is_bracket, self.is_result)

    def generate_data(self):
        '''根据条件生成所需口算题'''

        slist = []
        k = 0
        # 循环生成所有加法口算题

        while True:

            formula = self.__getFormula()  # 生成一道算式题
            if formula:
                slist.append(formula)
                k += 1  # 成功添加一道
            if k == self.number:
                break

        random.shuffle(slist)  # 洗牌，先打乱list中的排序
        self.__data_list = random.sample(slist, self.number)  # 随机取需要的口算题量。
        return self.__data_list

    def produce(self):
        '''打印预览预留接口'''
        pass

    def test(self):
        '''测试使用'''
        pass

    def get_answer(self):
        '''生成口算题答案'''
        answer_list = []
        for item in self.__data_list:
            answer = item.replace("x", "*").replace("÷", "/").replace("=", "")
            r = eval(answer)
            if re.match("\d+\.0$", str(r)):
                answer += "=" + str(int(r))
            else:
                answer += "=" + str(r)
            answer_list.append(answer.replace("*", "x").replace("/", "÷"))
        return answer_list


@get_time
def main():
    add = {"carry": 1, }  # 加法设置
    sub = {"abdication": 1, }  # 减法设置
    mult = { }  # 乘法设置
    div = { }  # 除法设置

    signum = 4
    step = 2
    is_result = 0
    number = 20
    is_bracket = 1

    multistep = [[1, 99], [1, 99], [1, 9], [1, 9], [0, 9], ]

    symbols = [[1, 2], [4], [2, ]]

    g = Generator(add, sub, mult, div, signum, step, number, is_result, is_bracket, multistep, symbols)

    datalist = g.generate_data()
    print(datalist)


if __name__ == '__main__':
    main()  # 程序入口
