#!/usr/bin/env python3
# -*- coding=utf-8 -*-


__version__ = "1.0.0"

__all__ = ['is_int','get_num','is_subnocarry','is_multcarry',
           'is_addcarry','is_addnocarry','getOneAdd',]

import random


########加法相关判断设置##########


def getOneAdd(formulas,result,carry,is_result):
    '''
    根据条件生成一道一步加法算式题
    :param formulas:
    :param carry
    :return: bool or str 成功返回一个符合条件的加法算数题str，失败返回False
    '''
    a,b = formulas[0],formulas[1]
    if a+b>=result :
        if carry == 1:#随机
            return getAddstr(a,b)
        elif carry == 2:#进位
            if is_addcarry(a,b):
                return getAddstr(a,b)
            else:
                return False
        elif carry == 3:#不进位
            if is_addnocarry(a,b):
                return getAddstr(a,b)
            else:
                return False
    else:
        return False

def getAddstr(a,b,is_result):
    '''
    返回一道加法题str
    :param a: int
    :param b: int
    :return: str
    '''
    if is_result == 1:#求结果
        return "{}+{}=".format(a, b)
    elif is_result == 2:#求运算项
        #随机分配求运算项
        rst = a+b
        if random.randint(0,1) > 0:
            a = "_"
            return "{}+{}={}".format(a, b,rst)
        else:
            b = "_"
            return "{}+{}={}".format(a, b, rst)


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


def is_subnocarry(a, b):
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

def is_subnocarry(a,b):
    '''
    判断减法无退位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    return not is_subnocarry(a,b)

########乘法相关判断设置##########

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

