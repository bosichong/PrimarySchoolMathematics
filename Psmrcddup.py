#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-10-18
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python实现小学生加减乘除速算考试题卷。
# @Url     : http://www.17python.com/blog/29
# @Details : Python实现小学生加减乘除速算考试题卷。
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# 用Python自动生成小学生加减乘除口算考试题卷。
###################################


'''
孩子上小学一年级了，加减乘除的口算就要开始练习了，估计老题肯定会让家长出题，所以提前准备一下，利用Python开发了一套自动生成小学生口算题的小应用。而且今天是程序员节，撸200行代码庆祝一下。：）
程序核心功能：1.根据条件生成相关的口算题，2.保存为排版好的网页用来打印。

其实一开始以为很简单的一个小应用了，结果发现编写起来好多的条件需要判断，不过这也算是一份不错的python复习案例了，几乎把一些常用的python语法都用到了。
目前只实现了单步加减法口算题的生成，配置项实现了口算题的数值范围取向，比如0-20之间的加减法，还可以过滤不需要的数字，判断加法进位减法退位，以及一些配置上错误时的判断：
比如设置0-5范围内，要生成进位加法20道，这是不可能实现的。
比如有意思的是加减法进退位的判断，程序中我写了一个简单方法。
开始以为单步和多步计算可以使同一方法，现在看来还得需要分开来写，如果要硬挤到一起方法就会太复杂了，不易梳理。
后续会把功能上分成 单步 二步 三步（加减乘除）法，乘除法相对来说简单些，除法要判断是否有余，有求余数口算？
而且原以为打印这个功能很简单的，其实如果做起来排版也是挺麻烦的，后继会慢慢更新程序并制作出适合的排版方式。
'''

import random

class Generator(object):
    '''
    - @sigunm   int
        运算符 (1: 加, 2: 减, 3: 乘, 4: 除)
    - @range    tuple
        随机范围, 默认: (0, 10)
    - @need_carry    int
        进位, 退位运算(1: 随机, 2: 进位, 3: 退位), 默认: 1
        进位: 加法和乘法运算时, 才会产生进位
        退位: 减法和出发运算时, 才会产生退位
    - @step int
        生成几步运算, 默认: 1
    - @filter tuple
        需要过滤的值
    - @same boolean
        是否相同
    - @intFlag boolean
        减法运算时表示是否允许产生负数运算题
        除法运算时表示是否允许产生小数运算
        默认: False
    - @intFlag int
        需要生成的题数量
        默认：80
    '''

    signum = None
    range = None
    need_carry = None
    step = None
    filter = None
    same = None
    intFlag = None
    number =None

    def __init__(self, signum=None, range=(0, 10), need_carry=1, step=1, filter=(0, 10), same=True, intFlag=False,num=80):
        if signum is None:
            raise Exception("required param signum is missing or signum is None")
        if signum not in (1,2,3,4):
            raise Exception("param signum must be 1 or 2 or 3 or 4")
        if range is None:
            raise Exception("required param range is missing or range is None")
        if need_carry not in (1, 2, 3):
            need_carry = 1
        # step 参数暂时默认为 1
        step = 1
        if (signum == 1 or signum == 3) and need_carry == 3:
            raise Exception("非法配置参数, 加法和乘法运算不会产生退位")
        if (signum == 2 or signum == 4) and need_carry == 2:
            raise Exception("非法配置参数, 减法和除法运算不会产生进位")

        self.__init(signum, range, need_carry, step, filter, same, intFlag,num)

    def __init(self, signum=None, range=(0, 10), need_carry=1, step=1, filter=(0, 10), same=True, intFlag=2, num=80):
        '''初始化参数配置'''
        if signum == 1:
            self.signum = "+"
        elif signum == 2:
            self.signum = "-"
        elif signum == 3:
            self.signum = "*"
        elif signum == 4:
            self.signum = "/"

        self.range = range
        self.need_carry = need_carry
        self.step = step
        self.filter = filter
        self.intFlag = intFlag

        self.min = min(range)
        self.max = max(range)
        self.number = num
        self.__data_list = []#生成的口算题

    def __is_valid(self, a, b):
        '''校验生成数值是否符合配置要求'''
        if self.need_carry == 1:
            r = eval("{}{}{}".format(a, self.signum, b))
            if self.intFlag:
                is_int = isinstance(r, int)
                if self.signum == "-" and r > 0:
                    return True
                elif self.signum == "/" and is_int:
                    return True
                else:
                    return False
            else:
                return True
        if self.need_carry == 2 and (self.signum == "+" or self.signum == "*") and ( len(str(eval("{}{}{}".format(a, self.signum, b)))) > max(len(str(a)), len(str(b))) ):
            return True
        elif self.need_carry == 3 and (self.signum == "-" or self.signum == "/"):
            r = eval("{}{}{}".format(a, self.signum, b))
            if self.intFlag:
                is_int = isinstance(r, int)
                if self.signum == "-" and r > 0 and len(str(r)) < min(len(str(a)), len(str(b))):
                    return True
                elif self.signum == "/" and is_int and len(str(r)) < min(len(str(a)), len(str(b))) :
                    return True
                else:
                    return False
            else:
                # 此处还需判断是否退位
                is_int = isinstance(r, int)
                if is_int and len(str(r)) < min(len(str(a)), len(str(b))):
                    return True
                elif is_int == False and len(str(int(r))) < min(len(str(a)), len(str(b))):
                    return True
                return False
        else:
            return False

    def __get_num(self, number):
        '''反回一个整数的个位数'''
        value0 = number / 10
        value0 = int(value0)
        return number - value0 * 10

    def __is_carry(self, a, b):
        '''判断加法是否存在进位'''
        if (self.__get_num(a) + self.__get_num(b) < 10):
            return False
        else:
            return True

    def __get_topic(self, a, b):
        '''根据两个数字返回一道单步口算加法题'''
        if a != b and not (a in self.filter) and not (b in self.filter):
            if self.__is_valid(a, b):
                if(self.signum == '*'):
                    return "{}{}{}=".format(a, '×', b)
                if (self.signum == '/'):
                    return "{}{}{}=".format(a, '÷', b)
                else:
                    return "{}{}{}=".format(a, self.signum, b)
        else:
            return False

# <<<<<<< HEAD:Psmrcddup.py
#     def __generate_data(self):
# =======
    def generate_data(self):
# >>>>>>> 1ce8585c602f7d4523a1273d5e0293769b9bf0b0:Psm-rcddup.py
        '''根据条件生成所需数据列表'''
        # 循环生成所有加法口算题
        for i in range(self.min, self.max):
            for j in range(self.min, self.max):
                addt = self.__get_topic(i, j)
                if addt:
                    self.__data_list.append(addt)
        if (len(self.__data_list) >= self.number):
            random.shuffle(self.__data_list)  # 洗牌，先打乱list中的排序
            self.__data_list = random.sample(self.__data_list, self.number)  # 随机取需要的口算题量。
        elif(len(self.__data_list) == 0):
            raise Exception('此数字范围内生成的加法口算题未能达到您要求的数目，请检查配置以适合程序的生成，请修改数值符合加法进位')
        else:
            if self.same:
                for i in range(self.number - len(self.__data_list)):
                    k = random.randint(0, len(self.__data_list) - 1)
                    self.__data_list.append(self.__data_list[k])
            else:
                raise Exception('此数字范围内生成的加法口算题未能达到您要求的数目，请检查配置以适合程序的生成，比如设置可以生成相同的题')
        return self.__data_list

    def produce(self):
        self.generate_data()
        # print(self.__data_list)
        return self.__data_list
        '''打印预览预留接口'''


def main():
    data_list = []
    g_add = Generator(signum=1, range=(0, 20), need_carry=1, step=1, filter=(0, 10), same=True)
    g_add_data = g_add.generate_data(20)
    data_list.extend(g_add_data)
    # 生成减法口算题
    g_sub = Generator(signum=2, range=(0, 20), need_carry=1, step=1, filter=(0, 10), same=True)
    g_sub_data = g_sub.generate_data(20)
    data_list.extend(g_sub_data)
    # 打印数据
    print(data_list)
    

if __name__ == '__main__':
    main()  # 程序入口