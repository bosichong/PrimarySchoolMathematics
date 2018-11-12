#!/usr/bin/env python3
# -*- coding=utf-8 -*-


__version__ = "1.0.0"

__all__ = [

            'is_int','get_num','is_abdication','is_multcarry','getRandomNum',
           'is_addcarry','is_addnocarry',
           'getOneAdd','getOneSub','getOneMult','getOneDiv'

           ]

import random


########加法相关判断设置##########


def getOneAdd(formulas,result,carry,is_result):
    '''
    根据条件生成一道一步加法算式题
    :param formulas: 给定的单步加法的两个值
    :param carry: int 加法进位
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的加法算数题str，失败返回False
    '''
    a,b = formulas[0],formulas[1]

    if result[0] < a+b < result[1]:
        if carry == 1:#随机
            return getOneStr(a,b,is_result,"+")
        elif carry == 2:#进位
            if is_addcarry(a,b):
                return getOneStr(a, b, is_result, "+")
            else:
                return False
        elif carry == 3:#不进位
            if is_addnocarry(a,b):
                return getOneStr(a, b, is_result, "+")
            else:
                return False
    else:
        return False



def is_addcarry(a, b,signum):
    '''
    判断加法进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''

    if (get_num(a) + get_num(b) < 10):
        return False
    else:
        return True


def is_addnocarry(a, b):
    '''
    判断加法无进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    return not is_addcarry(a,b)

########减法相关判断设置##########



def getOneSub(formulas,result,carry,is_result):
    '''
    根据条件生成一道一步减法算式题
    :param formulas: 给定的单步减法的两个值
    :param carry: int 减法退位
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的减法算数题str，失败返回False
    '''
    a,b = formulas[0],formulas[1]
    if result[0] < a-b < result[1]:
        if carry == 1:#随机
            return getOneStr(a,b,is_result,"-")
        elif carry == 2:#退位
            if is_abdication(a,b):
                return getOneStr(a, b, is_result, "-")
            else:
                return False
        elif carry == 3:#不退位
            if is_noabdication(a,b):
                return getOneStr(a, b, is_result, "-")
            else:
                return False
    else:
        return False



def is_abdication(a, b):
    '''
    判断减法退位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''

    if (get_num(a) < get_num(b)):
        return True
    else:
        return False

def is_noabdication(a,b):
    '''
    判断减法无退位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    return not is_abdication(a,b)

########乘法相关判断设置##########

def getOneMult(formulas,result,is_result):
    '''
    根据条件生成一道一步乘法算式题
    :param formulas: 给定的单步乘法的两个值
    :param result : int 结果值最大范围
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的减法算数题str，失败返回False
    '''
    a,b = formulas[0],formulas[1]
    if result[0] < a*b < result[1]:
        return getOneStr(a,b,is_result,"*")
    else:
        return False



def is_multcarry(a, b):
    '''
    判断乘法和乘法是否存在进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''

    if (get_num(a) * get_num(b) < 10):
        return False
    else:
        return True

########除法相关判断设置##########


def getOneDiv(formulas,result,is_result):
    '''
    根据条件生成一道一步除法算式题
    :param formulas: 给定的单步除法的两个值
    :param result : int 结果值最大范围
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的减法算数题str，失败返回False
    '''
    a,b = formulas[0],formulas[1]
    if (result[0] < a/b < result[1]) and b > 0 and (a%b == 0) : #并且整除
        return getOneStr(a,b,is_result,"/")
    else:
        return False


def is_int(num):
    '''
    判断一个数是否为整数
    :param num: int
    :return: boolean
    '''
    return isinstance(num , int)


def get_num(number):
    '''
    反回一个整数的个位数
    :param number: int
    :return: int
    '''
    value0 = number / 10
    value0 = int(value0)
    return number - value0 * 10



def getOneStr(a,b,is_result,signum):
    '''
    返回一道单步算式题str（可以返回+-*/单步算试题）
    :param a: int
    :param b: int
    :return: str
    '''
    if signum == "*":
        signum = "x"
    elif signum == "/":
        signum = "÷"
    if is_result == 1:#求结果
        return "{}{}{}=".format(a,signum, b)
    elif is_result == 2:#求运算项
        #随机分配求运算项
        rst = a+b
        if random.randint(0,1) > 0:
            a = "_"
            return "{}{}{}={}".format(a, signum,b,rst)
        else:
            b = "_"
            return "{}{}{}={}".format(a, signum,b, rst)



def getRandomNum(list, step):
    '''

    Author  : andywu1998
    Mail    : 1078539713@qq.com
    返回一组算式项

    '''
    newList = []
    for i in range(0, step+1):
        newList.append(random.randint(list[i][0], list[i][1]))
    return newList

def main():
    lr = [[1, 9], [1, 9], [1, 9], [1, 9]]
    step = 1

    print(getRandomNum(lr,step))


    # print(getOneAdd([3, 9], [1, 20],1, 2))
    # print(getOneSub([9, 3], [1, 20],1, 1))
    # print(getOneMult([3,9],[21,81],2))
    # print(getOneDiv([9, 3], [1, 9], 1))



if __name__ == '__main__':
    main()

