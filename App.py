#!/usr/bin/env python3
# -*- coding=utf-8 -*-

'''

临时程序入口
后续会写一个类，用来配置口算题生成前的配置，然后配以GUI实现可视化配置。

'''
import random

from Psmrcddup import Generator
from PrintPreview import PrintPreview


def main():
    print('程序开始运行')
    sets = 3  # 三套题
    psm_list =[]

    # 每套题包括的内容，至少有一种题型，每套题的总数量为几种题型的数量总合。
    #
    # - @sigunm   int
    #     运算符 (1: 加, 2: 减, 3: 乘, 4: 除)
    # - @range    tuple
    #     随机范围, 默认: (0, 10)
    # - @need_carry    int
    #     进位, 退位运算(1: 随机, 2: 进位, 3: 退位), 默认: 1
    #     进位: 加法和乘法运算时, 才会产生进位
    #     退位: 减法和出发运算时, 才会产生退位
    # - @step int
    #     生成几步运算, 默认: 1
    # - @filter tuple
    #     需要过滤的值
    # - @same boolean
    #     是否相同
    # - @intFlag boolean
    #     减法运算时表示是否允许产生负数运算题
    #     除法运算时表示是否允许产生小数运算
    #     默认: False
    # - @intFlag int
    #     需要生成的题数量
    #     默认：80

    # 配置每套题包括的内容，至少有一种题型，每套题的总数量为几种题型的数量总合。
    psm_type = [
        [1, (0, 20), 1, 1, (0, 1), True, False, 25],
        [2, (0, 20), 1, 1, (0, 1), True, False, 25],
        [3, (0, 9), 1, 1, (0,), True, False, 25],
        [4, (0, 81), 1, 1, (0, 1), True, False, 25]
    ]

    #循环生成每套题
    for i in range(sets):
        templist = []
        for l in psm_type:
            g = Generator(signum=l[0], range=l[1], need_carry=l[2], step=l[3], filter=l[4], same=l[5],num=l[7])
            templist = templist+g.produce()
        random.shuffle(templist)
        print(templist)
        psm_list.append(templist)
    #这里的标题后继需要进行判断进行起名，暂时固定
    pp = PrintPreview(psm_list, ['小学生口算题','小学生口算题','小学生口算题'], 4)
    pp.produce()#生成docx


if __name__ == '__main__':
    main()
