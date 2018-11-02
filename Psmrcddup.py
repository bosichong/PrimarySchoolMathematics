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

    2.保存为.docx用来打印.


开心Python Django 学习交流q群：217840699


Author  : J.sky
Mail    : bosichong@qq.com

Author  : rcddup
Mail    : 410093793@qq.com

'''

import random
import re

class Generator(object):
    '''
    - @sigunm   int
        运算符 (1: 加, 2: 减, 3: 乘, 4: 除)
    - @range    tuple
        随机范围, 默认: (0, 10)
    - @need_carry    int
        进位, 退位运算(1: 随机, 2: 进位, 3: 退位, 4:不进位也不退位), 默认: 1
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
    - @num int
        需要生成的题数量
        默认：80
    '''

    signum = None
    range = None
    need_carry = None
    step = None
    filter = None
    same = None
    # intFlag = None
    number = None

    def __init__(self, signum=None, range=(0, 10), need_carry=1, step=1, filter=(0, 10), same=True,
                 num=80):
        if signum is None:
            raise Exception("required param signum is missing or signum is None")
        if signum not in (1, 2, 3, 4):
            raise Exception("param signum must be 1 or 2 or 3 or 4")
        if range is None:
            raise Exception("required param range is missing or range is None")
        if need_carry not in (1, 2, 3, 4):
            need_carry = 1
        # step 参数暂时默认为 1
        step = 1
        if (signum == 1 or signum == 3 or signum == 4) and need_carry == 3:
            raise Exception("非法配置参数, 加法和乘法运算不会产生退位，除法暂时不考虑退位")
        if (signum == 2 or signum == 4) and need_carry == 2:
            raise Exception("非法配置参数, 减法和除法运算不会产生进位")
        if (signum == 3 or signum == 4) and need_carry == 4:
            raise Exception("非法配置参数, 乘法和除法运算不暂时不锁定不进位不退位")

        self.__init(signum, range, need_carry, step, filter, same, num)

    def __init(self, signum=None, range=(0, 10), need_carry=1, step=1, filter=(0, 10), same=True,num=80):
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

        self.same =same
        self.min = min(range)
        self.max = max(range)
        self.number = num
        self.__data_list = []   # 生成的口算题

    def __is_int(self, num):
        '''判断一个数是否为整数'''
        num_str = str(num)
        num_strs = num_str.split(".")
        if len(num_strs) == 1:
            return True
        elif len(num_strs) == 2 and num_strs[1] == "0":
            return True
        return False

    def __is_valid(self, a, b):
        '''校验生成数值是否符合配置要求'''
        if self.need_carry == 1:  # 随机无论进退位时的判断
            # 加法与乘法无所谓
            if self.signum == "+" or self.signum == "*":
                return True

            if self.signum == "-" and a > b:  # 避免减法出现结果为0或负数的题型
                return True

            if self.signum == "/" and a > b and b!=0:  # 修改判断除法结果大于1 除数不能为0 避免出现10/10 20/20 这种题型。
                r = eval("{}{}{}".format(a, self.signum, b))
                is_int = self.__is_int(r)
                if self.signum == "/" and is_int:  # 必须是整数
                    return True
                else:
                    return False
            else:
                return False

        # 选定加法不进位或减法不退位的判断
        if self.need_carry == 4:
            if self.signum == "+":
                return self.__is_nocarry(a, b)

            if a>b and self.signum == "-":
                return self.__is_nocarry(a, b)

        # 加法和乘法必须为进位时的判断
        if self.need_carry == 2 and (self.signum == "+" or self.signum == "*") and self.__is_carry(a, b):
            return True
        # 减法必须为退位的判断
        if self.need_carry == 3 and self.signum == "-" and a > b and self.__is_s_nocarry(a, b):
            return True

        else:
            return False

    def __get_num(self, number):
        '''反回一个整数的个位数'''
        value0 = number / 10
        value0 = int(value0)
        return number - value0 * 10

    def __is_carry(self, a, b):
        '''判断加法和乘法存在进位'''
        if self.signum == '+':
            if (self.__get_num(a) + self.__get_num(b) < 10):
                return False
            else:
                return True
        if self.signum == '*':
            if (self.__get_num(a) * self.__get_num(b) < 10):
                return False
            else:
                return True

    def __is_nocarry(self, a, b):
        '''判断加法无进位，减法无退位'''
        if self.signum == '+':
            if (self.__get_num(a) + self.__get_num(b) < 10):
                return True
            else:
                return False
        if self.signum == '-':
            if (self.__get_num(a) >= self.__get_num(b)):
                return True
            else:
                return False

    def __is_s_nocarry(self, a, b):
        '''判断减法有退位'''
        if self.signum == '-':
            if (self.__get_num(a) < self.__get_num(b)):
                return True
            else:
                return False

    def __get_topic(self, a, b):
        '''根据两个数字返回一道单步口算题'''
        if self.__is_valid(a, b):
            if (self.signum == '*'):
                return "{}{}{}=".format(a, '×', b)
            if (self.signum == '/'):
                return "{}{}{}=".format(a, '÷', b)
            else:
                return "{}{}{}=".format(a, self.signum, b)

    def generate_data(self):
        '''根据条件生成所需数据列表'''

        slist = []

        # 循环生成所有加法口算题
        for i in range(self.min, self.max):
            for j in range(self.min, self.max):
                if (i in self.filter) or (j in self.filter):
                    continue
                addt = self.__get_topic(i, j)
                if addt:
                    slist.append(addt)

        if (len(slist) >= self.number):
            random.shuffle(slist)  # 洗牌，先打乱list中的排序
            self.__data_list = random.sample(slist, self.number)  # 随机取需要的口算题量。

            return self.__data_list
        if (len(slist) == 0):
            raise Exception('此数字范围内生成的加法口算题未能达到您要求的数目，请检查配置以适合程序的生成，请修改数值符合加法进位')
        else:
            if self.same:
                for i in range(self.number - len(slist)):
                    k = random.randint(0, len(slist)-1)
                    slist.append(slist[k])
                return slist
            else:

                raise Exception('此数字范围内生成的加法口算题未能达到您要求的数目，请检查配置以适合程序的生成，比如设置可以生成相同的题')

    def produce(self):
        '''打印预览预留接口'''
        pass

    def test(self):
        print(self.__is_nocarry(9,9))

    def get_answer(self):
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
    g_add = Generator(signum=1, range=(0, 20), need_carry=1, step=1, filter=(0, 1), same=True, num=20)
    g_add_data = g_add.generate_data()
    print(g_add_data)
    # data_list.extend(g_add_data)
    # 生成减法退位口算题
    g_sub = Generator(signum=2, range=(0, 20), need_carry=1, step=1, filter=(0, 1), same=True, num=20)
    g_sub_data = g_sub.generate_data()
    print(g_sub_data)
    # data_list.extend(g_sub_data)
    # # 生成乘法口算题
    g_multi = Generator(signum=3, range=(0, 8), need_carry=2, step=1, filter=(0,1), same=True, num=20)
    g_multi_data = g_multi.generate_data()
    print(g_multi_data)
    # data_list.extend(g_multi_data)
    # 生成除法口算题
    g_div = Generator(signum=4, range=(0, 81), need_carry=1, step=1, filter=(0, 1), same=True, num=20)
    g_div_data = g_div.generate_data()
    print(g_div_data)
    # 生成口算题答案
    g_div_answer_list = g_div.get_answer()
    print(g_div_answer_list)
    # data_list.extend(g_div_data)
    # 打印数据
    # print(data_list)
    g_add.test()


if __name__ == '__main__':
    main()  # 程序入口
