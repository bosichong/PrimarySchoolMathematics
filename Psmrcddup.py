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

'''

import random
import re

from utils.PSM_help import *

__version__ = "0.1.0"


class Generator(object):
    '''
    口算题生器核心类，负责生成完整的口算题
    '''

    addattrs = None
    subattrs = None
    multattrs = None
    divattrs = None

    signum = None
    range = None
    step = None
    same = None
    number = None

    is_bracket =None
    symbols = None



    def __init__(self, addattrs=None, subattrs=None, multattrs=None, divattrs=None,
                 signum=None,step=1, same=True, num=80,
                 is_bracket = False, _symbols=None):
        '''
        :param addattrs: list 加法设置属性，
        包括 四项运算项及结果数值范围设置，进位随机选择项单选，随机1，进位2，不进位3

        :param subattrs: list 减法设置属性，
        包括 四项运算项及结果数值范围设置，退位随机选择项单选，随机1，退位2，不退位3

        乘除法暂略

        :param signum: list 包含题型需要的 1+ 2- 3* 4/
        :param range: boolean
        :param step: int 生成几步运算, 默认: 1 取值范围 1-3


        :param is_bracket: boolean 是否需要括号
        :param symbols: list 默认包括三组list,分别代表123步算式需要题型种类+-*/
        :param num:
        '''

        # step 参数暂时默认为 1
        step = 1
        if step is None:
            raise Exception("required param signum is missing or signum is None")
        if step not in (1, 2, 3):
            raise Exception("param signum must be 1 or 2 or 3")

        self.__init(signum, range, step, filter, same, num)

    def __init(self, signum=None, range=(0, 10), need_carry=1, step=1, filter=(0, 10), same=True, num=80):
        '''初始化参数配置'''

        self.range = range
        self.need_carry = need_carry
        self.step = step
        self.filter = filter

        self.same = same
        self.min = min(range)
        self.max = max(range)
        self.number = num
        self.__data_list = []  # 生成的口算题

    def __isValid(self, a, b):
        '''校验生成数值是否符合配置要求'''
        if self.need_carry == 1:  # 随机无论进退位时的判断
            # 加法与乘法无所谓
            if self.signum == "+" or self.signum == "*":
                return True

            if self.signum == "-" and a > b:  # 避免减法出现结果为0或负数的题型
                return True

            if self.signum == "/" and a > b and b != 0:  # 修改判断除法结果大于1 除数不能为0 避免出现10/10 20/20 这种题型。
                r = eval("{}{}{}".format(a, self.signum, b))
                isint = is_int(int(r))
                if self.signum == "/" and isint:  # 必须是整数
                    return True
                else:
                    return False
            else:

                return False

        # 选定加法不进位或减法不退位的判断
        if self.need_carry == 4:
            if self.signum == "+":
                return self.__isNocarry(a, b)

            if a > b and self.signum == "-":
                return self.__isNocarry(a, b)

        # 加法和乘法必须为进位时的判断
        if self.need_carry == 2 and (self.signum == "+" or self.signum == "*") and self.__isCarry(a, b):
            return True
        # 减法必须为退位的判断
        if self.need_carry == 3 and self.signum == "-" and a > b and is_subnocarry(a, b, self.signum):
            return True

        else:
            return False

    def __isCarry(self, a, b):
        '''判断加法和乘法存在进位'''
        if self.signum == '+':
            return is_addcarry(a, b, self.signum)
        if self.signum == '*':
            return is_multcarry(a, b, self.signum)

    def __isNocarry(self, a, b):
        '''判断加法无进位，减法无退位'''
        if self.signum == '+':
            return is_addnocarry(a, b, self.signum)
        if self.signum == '-':
            return is_subnocarry(a, b, self.signum)

    def __getFormula(self, a, b):
        '''根据给出的属性返回一道合法的口算题'''


        # if self.__is_valid(a, b):
        #     if (self.signum == '*'):
        #         return "{}{}{}=".format(a, '×', b)
        #     if (self.signum == '/'):
        #         return "{}{}{}=".format(a, '÷', b)
        #     else:
        #         return "{}{}{}=".format(a, self.signum, b)


    def generate_data(self):
        '''根据条件生成所需口算题'''

        slist = []

        # 循环生成所有加法口算题
        for i in range(self.number):
            formula = self.__getFormula(i, j)
            if formula:
                slist.append(formula)



        if (len(slist) >= self.number):
            random.shuffle(slist)  # 洗牌，先打乱list中的排序
            self.__data_list = random.sample(slist, self.number)  # 随机取需要的口算题量。

            return self.__data_list
        if (len(slist) == 0):
            raise Exception('此数字范围内生成的加法口算题未能达到您要求的数目，请检查配置以适合程序的生成，请修改数值符合加法进位')
        else:
            if self.same:
                for i in range(self.number - len(slist)):
                    k = random.randint(0, len(slist) - 1)
                    slist.append(slist[k])
                self.__data_list = slist
                return self.__data_list
            else:

                raise Exception('此数字范围内生成的加法口算题未能达到您要求的数目，请检查配置以适合程序的生成，比如设置可以生成相同的题')

    def produce(self):
        '''打印预览预留接口'''
        pass

    def test(self):
        print(self.__is_nocarry(9, 9))

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


def main():
    data_list = []
    # 生成加法进位口算题
    g_add = Generator(signum=1, range=(0, 9), need_carry=1, step=1, filter=(0, 1), same=True, num=20)
    g_add_data = g_add.generate_data()
    print(g_add_data)


if __name__ == '__main__':
    main()  # 程序入口
