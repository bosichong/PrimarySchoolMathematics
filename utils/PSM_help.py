#!/usr/bin/env python3
# -*- coding=utf-8 -*-
'''
开心Python Django 学习交流q群：217840699


Author  : J.sky
Mail    : bosichong@qq.com

Author  : rcddup
Mail    : 410093793@qq.com

Author  : andywu1998
Mail    : 1078539713@qq.com
'''

__version__ = "1.0.0"

__all__ = [

    'getPSMstr', 'getMoreStep', 'getOne','get_time','getRandomNum'

]

import random
import time
import re


def f1(s):
    '''
    搜索题中括号算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return:搜索括号算式
    '''
    ss = re.search("\(\d+[\+\-\*/\d]+\)", s)
    if ss:
        return ss.group(0)


def f2(s):
    '''
    搜索题中乘除法算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return: 乘除法算式
    '''
    ss = re.search("\d+[\*/]\d+", s)
    if ss:
        return ss.group(0)


def f3(s):
    '''
    搜索加减法算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return:加减法算式
    '''
    ss = re.search("\d+[\+\-]\d+", s)
    if ss:
        return ss.group(0)


def f4(s):
    '''
    搜索加减法乘除算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return: str 加减乘除算式
    '''
    ss = re.search("\d+[\+\-\*/\d]+", s)
    if ss:
        return ss.group(0)


def validator(s, result, carry, abdication):
    '''
    算式分解校验器
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return: bool
    '''

    if isResultOk(s, result):
        if f1(s):

            s = validator1(s, result, carry, abdication)

            if s:
                return validator2(s, result, carry, abdication)
            else:
                return False

        else:#校验无括号算式
            return validator2(s, result, carry, abdication)
    else:
        return False


def validator1(s, result, carry, abdication):
    '''
    算式分解校验器提取括号内算式，然后递归给validator2进行算式验证
    本方法可以递归提取括号嵌套算式
    Author  : J.sky
    Mail    : bosichong@qq.com
    :param s: 算式
    :return: bool
    '''
    while f1(s):
        fa = f1(s)
        fb = f4(f1(s))
        r = validator2(fb, result, carry, abdication)
        if r:
            s = s.replace(fa, "{}".format(int(float(r))))
        else:
            return False
    return s


def validator2(s, result, carry, abdication):
    '''
    分解乘除加减法计算结果并校验
        Author  : J.sky
    Mail    : bosichong@qq.com
    :param s:
    :return:
    '''

    # 乘除法验证
    while f2(s):
        f = f2(s)
        if isMultDivOk(f, result):
            r = eval(f)
            s = s.replace(f, str(int(float(r))))
            # print(r,s)
        else:
            return False
    # 加减法验证
    while f3(s):
        f = f3(s)
        # print(f)
        if isAddSub(f, result, carry, abdication):
            r = eval(f)
            s = s.replace(f, str(r))
        else:
            return False

    return s


def isResultOk(str, result):
    '''


    验证算式结果是否正确

    Author  : J.sky
    Mail    : bosichong@qq.com



    :param str: 一道算式题
    :param list 结果范围
    :return: bool
    '''
    # print('比较结果：',eval(str),result[0] <= eval(str) <= result[1])
    return result[0] <= eval(str) <= result[1]


def isMultDivOk(s, result):
    '''
    判断乘除法正确性
    :param str: 算式
    :param result list 结果范围
    :return: bool
    '''
    if re.search("/", s):
        divs = re.split("/", s)
        if int(divs[1]) == 0:
            return False
        else:
            if isResultOk(s, result) and ((int(divs[0]) % int(divs[1])) == 0) and eval(s) > 0 : # 除法，除数不能为0，并且结果在范围内,并且整除无余数
                return True
            else:
                return False
    if re.search("\*", s):
        return isResultOk(s, result)  # 乘法结果在范围内


def isAddSub(s, result, carry, abdication):
    '''
    判断加减法正确性
    :param s: str 算式
    :param result: list 结果范围
    :param carry: int 1，2，3 随机 进位 不进位
    :param abdication: int 1，2，3 随机，退位，不退位
    :return: bool
    '''
    tmp = re.split("[\+\-]", s)
    if isResultOk(s, result):
        if re.search("\+", s):

            if carry == 1:
                return True
            elif carry == 2:
                return is_addcarry(int(tmp[0]), int(tmp[1]))
            elif carry == 3:
                # print("加法进位校验")
                return is_addnocarry(int(tmp[0]), int(tmp[1]))

        elif re.search("\-", s):
            # print("减法校验开始")
            if abdication == 1:
                return True
            elif abdication == 2:
                return is_abdication(int(tmp[0]), int(tmp[1]))
            elif abdication == 3:
                return is_noabdication(int(tmp[0]), int(tmp[1]))
        else:
            return False


def getOne(formulas, signum, result, carry, abdication, is_result):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    根据条件生成一道一步算式题
    :param formulas: 给定的单步加法的两个值
    :param signum int 加减乘除
    :param result list 结果范围
    :param carry: int 加法进位
    :param is_result: 求结果或求运算项
    :return: bool or str 成功返回一个符合条件的加法算数题str，失败返回False
    '''
    return getMoreStep(formulas, result, [[signum], ], 1, carry, abdication, 0, is_result)


def getMoreStep(formulas, result, symbols, step, carry, abdication, is_bracket, is_result, ):
    '''


    Author  : J.sky
    Mail    : bosichong@qq.com

    :param formulas: list 整数算数项
    :param result: list 最终结果范围
    :param symbols: list 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
    :param step int 步数
    :param carry: int 加法是否进位
    :param abdication: int 减法是否退位
    :param is_bracket: int 是否包含括号
    :param is_result: int 求结果，求运算项
    :return: str 一道符合规则的口算运算题
    '''
    f = getRandomNum(formulas, step)
    str = getPSMstr(f, symbols, step, is_bracket)
    # print(str)
    if validator(str, result, carry, abdication):
        return getXStepstr(str, is_result)

    else:
        # print("校验失败")
        return False


def getPSMstr(formulas, symbols, step, is_bracket):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    生成算式题
    :param formulas: list 给定的算数项列表
    :param symbols: list 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
    :param step: int 步数
    :param is_bracket: int  括号
    :return:
    '''
    ss = ""
    sym = getRandomSymbols(symbols, step)
    for i in range(step):
        formulas.insert(i * 2 + 1, getSymbol(sym[i]))

    if is_bracket:
        k = getRandomBracket(step)  # 获得一个括号起始指针
        for i in range(2):

            if i == 0:
                formulas.insert(k + 4 * i, ('('))
            else:
                formulas.insert(k + 4 * i, (')'))

    for s in formulas:
        ss = ss + str(s)
    return ss


def getRandomBracket(step):
    '''
        Author  : J.sky
    Mail    : bosichong@qq.com
    返回一个括号起始随机数
    :param step:
    :return:
    '''
    while True:
        k = random.randint(0, step * 2 + 1 - 3)  # 获得一个括号起始指针
        if not k % 2:
            return k


########2步算式相关判断设置##########


def getXStepstr(src, is_result):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    给定一组算式和其结果，根据条件生成求结果或是求算数项的题型
    :param src: str 算式
    :param is_result: 0or1
    :return: str
    '''
    if is_result == 0:
        return repSymStr(src) + "="
    elif is_result == 1:
        return getRandomItem(repSymStr(src) + "=" + str(int(eval(src))))
    else:
        raise Exception("is_result求结果，求算数项参数设置错误！")


def repSymStr(s):
    '''
        Author  : J.sky
    Mail    : bosichong@qq.com
    更换乘除法符号
    :param s:
    :return:
    '''
    if re.search('\*', s):
        s = re.sub('\*', 'x', s)
    if re.search('/', s):
        s = re.sub('/', '÷', s)
    return s


def getRandomItem(sr):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    把得到的算式转变成求算数项口算题
    :param str: 一道算数题
    :return: str
    '''
    # print(sr)
    p = re.compile('\d+')
    sc = p.findall(sr)
    i = random.randint(0, len(sc) - 2)  # -2防止替换结果
    sr = sr.replace(sc[i], "__", 1)
    # print(sr)
    return sr


def getSymbol(sym):
    '''
    Author  : J.sky
    Mail    : bosichong@qq.com
    获得运算符号，用来运算结果
    :param sym: int
    :return: str
    '''
    if sym == 1:
        return "+"
    elif sym == 2:
        return "-"
    elif sym == 3:
        return "*"
    elif sym == 4:
        return "/"


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
    for i in range(step):
        index = random.randint(0, len(symbols[i]) - 1)
        newList.append(symbols[i][index])
    return newList


########加法相关判断设置##########


def is_addcarry(a, b, ):
    '''
    判断加法进位
    :param a: int
    :param b: int
    :param signum: str
    :return: boolean
    '''

    return (get_num(a) + get_num(b) > 10)


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


def getRandomNum(list, step):
    '''
    Author  : andywu1998
    Mail    : 1078539713@qq.com

    Author  : J.sky
    Mail    : bosichong@qq.com
    :param list:
    :param step:
    :return:
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
    # 加法进退位随机
    # print(getOne([[1, 9], [1, 9]], 1, [1, 20], 1, 1, 0))
    # print(getOne([[0, 9], [0, 9]], 2, [1, 20], 2, 2, 0))
    # print(getOne([[1, 9], [1, 9]], 3, [1, 81], 3, 1, 0))
    # print(getOne([[9, 81], [2, 9]], 4, [2, 9], 1, 1, 0))

    # 生成算式测试
    # print(getPSMstr([5,8,9,9,8],[[1,2],[1,],[2],[1,]],4,1))

    print(getMoreStep([[1, 55], [1, 99], [1, 99], [1, 9]], [1, 99], [[1, 3], [4], [4]], 2, 1, 1, 1, 0))

    # print(isMultDivOk('18/9',[1,99]))


if __name__ == '__main__':
    main()
