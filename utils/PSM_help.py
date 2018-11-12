#!/usr/bin/env python3
# -*- coding=utf-8 -*-


__version__ = "1.0.0"

__all__ = [

    'is_int', 'get_num', 'is_abdication', 'is_multcarry', 'getRandomNum', "get_time",
    'is_addcarry', 'is_addnocarry',
    'getOneAdd', 'getOneSub', 'getOneMult', 'getOneDiv',
    'getTwoStep',

]

import random
import time


########2步算式相关判断设置##########

def getTwoStep(formulas, result, symbols, carry, abdication, is_bracket, is_result, ):
    '''


    Author  : J.sky
    Mail    : bosichong@qq.com


    二步算式题生成
    :param formulas: list 返回3个整数算数项
    :param result: list 最终结果范围
    :param symbols: list 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
    :param carry: int 加法是否进位
    :param abdication: int 减法是否退位
    :param is_bracket: int 是否包含括号
    :param is_result: int 求结果，求运算项
    :return: str 一道符合规则的口算运算题
    '''

    a, b, c = formulas[0], formulas[1], formulas[2]#获取运算项的数值
    syms = getRandomSymbols(symbols,2)
    s1,s2 = syms[0],syms[1] #获取运算符号


    if is_bracket == 0:  # 无括号

        if(isItem(s1,a,b,result,carry,abdication)):#判断a与b的运算结果

            tp = eval(str(a)+getSymbol(s1)+str(b))#a与b的运算结果

            if (isItem(s1,tp,c,result,carry,abdication)):#判断第二步运算结果


                return "{}{}{}{}{}=".format(a,repSymbol(s1),b,repSymbol(s2),c,)
            else:
                return False
        else:
            return False


def repSymbol(signum):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com

    输出运算符号用来打印算式，主要处理*/法的符号
    :param signum:
    :return:
    '''
    if signum  == 1:
        return "+"
    elif signum == 2:
        return "-"
    elif signum == 3:
        return "x"
    elif signum == 4:
        return "÷"

def getSymbol(sym):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    获得运算符号，用来运算结果
    :param sym: int
    :return: str
    '''
    if sym  == 1:
        return "+"
    elif sym == 2:
        return "-"
    elif sym == 3:
        return "*"
    elif sym == 4:
        return "/"

def isItem(signum,a,b,result,carry,abdication):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com

    判断两个数成立的算式是否合法
    :param a:
    :param b:
    :param result:
    :param carry:
    :param abdication:
    :return: bool
    '''
    if signum == 1:
        return isTwoAdd(a,b,result,carry)
    elif signum == 2:
        return isTwoSub(a,b,result,abdication)
    elif signum == 3:
        return isTwoMult(a,b,result)
    elif signum == 4:
        return isTwoDiv(a,b,result)



def isTwoAdd(a,b,result,carry):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com

    判断两个数成立的加法算式是否合法

    :param a:
    :param b:
    :param result:
    :param carry:
    :return: bool
    '''
    return getOneAdd((a,b),result,carry,1)


def isTwoSub(a, b, result, abdication):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com

    判断两个数成立的减法算式是否合法

    :param a:
    :param b:
    :param result:
    :param carry:
    :return: bool
    '''
    return getOneSub((a, b), result, abdication, 1)


def isTwoMult(a, b, result, ):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com

    判断两个数成立的乘法算式是否合法

    :param a:
    :param b:
    :param result:
    :param carry:
    :return: bool
    '''
    return getOneMult((a, b), result, 1)

def isTwoDiv(a, b, result, ):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com

    判断两个数成立的除法算式是否合法

    :param a:
    :param b:
    :param result:
    :param carry:
    :return: bool
    '''
    return getOneDiv((a, b), result, 1)



def getRandomSymbols(symbols, step):
    '''

    Author  : J.sky
    Mail    : bosichong@qq.com

    返回一组运算符号

    :param symbols: list 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
    :param step: int 运算步
    :return:
    '''
    newList = []
    for i in range(0, step):
        index = random.randint(0, len(symbols[i])-1)
        newList.append(symbols[i][index])
    return newList


########加法相关判断设置##########


def getOneAdd(formulas, result, carry, is_result):
    '''
    根据条件生成一道一步加法算式题
    :param formulas: 给定的单步加法的两个值
    :param carry: int 加法进位
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的加法算数题str，失败返回False
    '''
    a, b = formulas[0], formulas[1]

    if result[0] < a + b < result[1]:
        if carry == 1:  # 随机
            return getOneStr(a, b, is_result, "+")
        elif carry == 2:  # 进位
            if is_addcarry(a, b):
                return getOneStr(a, b, is_result, "+")
            else:
                return False
        elif carry == 3:  # 不进位
            if is_addnocarry(a, b):
                return getOneStr(a, b, is_result, "+")
            else:
                return False
    else:
        return False


def is_addcarry(a, b, signum):
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
    return not is_addcarry(a, b)


########减法相关判断设置##########


def getOneSub(formulas, result, abdication, is_result):
    '''
    根据条件生成一道一步减法算式题
    :param formulas: 给定的单步减法的两个值
    :param carry: int 减法退位
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的减法算数题str，失败返回False
    '''
    a, b = formulas[0], formulas[1]
    if result[0] < a - b < result[1]:
        if abdication == 1:  # 随机
            return getOneStr(a, b, is_result, "-")
        elif abdication == 2:  # 退位
            if is_abdication(a, b):
                return getOneStr(a, b, is_result, "-")
            else:
                return False
        elif abdication == 3:  # 不退位
            if is_noabdication(a, b):
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


def is_noabdication(a, b):
    '''
    判断减法无退位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''
    return not is_abdication(a, b)


########乘法相关判断设置##########

def getOneMult(formulas, result, is_result):
    '''
    根据条件生成一道一步乘法算式题
    :param formulas: 给定的单步乘法的两个值
    :param result : int 结果值最大范围
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的减法算数题str，失败返回False
    '''
    a, b = formulas[0], formulas[1]
    if result[0] < a * b < result[1]:
        return getOneStr(a, b, is_result, "*")
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


def getOneDiv(formulas, result, is_result):
    '''
    根据条件生成一道一步除法算式题
    :param formulas: 给定的单步除法的两个值
    :param result : int 结果值最大范围
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的减法算数题str，失败返回False
    '''
    a, b = formulas[0], formulas[1]
    if (result[0] < a / b < result[1]) and b > 0 and (a % b == 0):  # 并且整除
        return getOneStr(a, b, is_result, "/")
    else:
        return False


########其它相关判断设置##########


def is_int(num):
    '''
    判断一个数是否为整数
    :param num: int
    :return: boolean
    '''
    return isinstance(num, int)


def get_num(number):
    '''
    反回一个整数的个位数
    :param number: int
    :return: int
    '''
    value0 = number / 10
    value0 = int(value0)
    return number - value0 * 10


def getOneStr(a, b, is_result, signum):
    '''
    返回一道单步算式题str（可以返回+-*/单步算试题）
    :param a: int
    :param b: int
    :return: str
    '''

    if is_result == 1:  # 求结果
        if signum == "*":
            signum = "x"
        elif signum == "/":
            signum = "÷"
        return "{}{}{}=".format(a, signum, b)
    elif is_result == 2:  # 求运算项
        # 随机分配求运算项
        rst = int(eval(str(a) + str(signum) + str(b)))
        if signum == "*":
            signum = "x"
        elif signum == "/":
            signum = "÷"
        if random.randint(0, 1) > 0:
            a = "_"
            return "{}{}{}={}".format(a, signum, b, rst)
        else:
            b = "_"
            return "{}{}{}={}".format(a, signum, b, rst)


def getRandomNum(list, step):
    '''

    Author  : andywu1998
    Mail    : 1078539713@qq.com
    返回一组算式项

    '''
    newList = []
    for i in range(0, step + 1):
        newList.append(random.randint(list[i][0], list[i][1]))
    return newList


# def get_timert(func):
#     '''定义一个程序运行时间计算装饰器有返回结果'''
#     def wrapper(*args, **kwargs):
#         start = time.time()#起始时间
#         res = func(*args, **kwargs)#要执行的函数
#         end = time.time()#结束时间
#         print('程序运行时间:{:.2f}ms'.format((end-start)*1000))
#         return res
#     return wrapper

def get_time(func):
    '''定义一个程序运行时间计算装饰器无返回结果'''

    def wrapper(*args, **kwargs):
        start = time.time()  # 起始时间
        func(*args, **kwargs)  # 要执行的函数
        end = time.time()  # 结束时间
        print('程序运行时间:{:.2f}ms'.format((end - start) * 1000))
        return func

    return wrapper


def main():



    print(getTwoStep([8,2,3],[1,50],[[1,2,3],[1,2]],1,1,0,1))
    print(getOneAdd([3, 9], [1, 20],1, 2))
    print(getOneSub([9, 3], [1, 20],1, 1))
    print(getOneMult([3,9],[21,81],2))
    print(getOneDiv([9, 3], [1, 9], 1))


if __name__ == '__main__':
    main()
