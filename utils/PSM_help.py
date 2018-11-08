#!/usr/bin/env python3
# -*- coding=utf-8 -*-


__version__ = "1.0.0"

__all__ = ['is_int','get_num','is_subnocarry','is_multcarry',
           'is_addcarry','is_addnocarry',]




########加法相关判断设置##########

def is_addcarry(a, b,signum):
    '''
    判断加法进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    if signum == '+':
        if (get_num(a) + get_num(b) < 10):
            return False
        else:
            return True


def is_addnocarry(a, b,signum):
    '''
    判断加法无进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    return not is_addcarry(a,b,signum)

########减法相关判断设置##########


def is_subnocarry(a, b,signum):
    '''
    判断减法退位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    if signum == '-':
        if (get_num(a) < get_num(b)):
            return True
        else:
            return False

def is_subnocarry(a,b,signum):
    '''
    判断减法无退位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    return not is_subnocarry(a,b,signum)

########乘法相关判断设置##########

def is_multcarry(a, b,signum):
    '''
    判断乘法和乘法是否存在进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    if signum == '*':
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
    num_str = str(num)
    num_strs = num_str.split(".")
    if len(num_strs) == 1:
        return True
    elif len(num_strs) == 2 and num_strs[1] == "0":
        return True
    return False


def get_num(number):
    '''
    反回一个整数的个位数
    :param number: int
    :return: int
    '''
    value0 = number / 10
    value0 = int(value0)
    return number - value0 * 10

