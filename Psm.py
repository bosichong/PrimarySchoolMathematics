# codeing=utf-8
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
孩子上小学一年级了，加减乘除的口算就要开始练习了，估计老题肯定会让家长出题，所以提前准备一下，利用Python开发了一套自动生成口算题的小应用。

程序核心功能：

题数，题类型（+-*/），数字范围，减法及除法算式的合法化判断，数学题排版及保存文件。

'''

import random


class PrimarySchoolMathematics:
    '''本程序核心类，负责生成算数题。'''

    # 总题数
    number = 60
    # 加法是否进位 是否进位：0进位1不进位2随机
    carry = 2
    # 减法是否退位：0退位1不退位2随机
    abdication = 0

    # 加法数字列表，最小数，最大数，过滤掉的数字,
    addlist = {'min': 0, 'max': 20, 'filter': [0, 1]}

    # 减法数字列表，最小数，最大数，过滤掉的数字
    subtractlist = {'min': 0, 'max': 20, 'filter': [0,1]}

    def addition(self):
        '''返回加法口算题'''

        additionlist = []
        for i in range(self.number):

            while (True):
                a = random.randint(self.addlist['min'], self.addlist['max'])
                b = random.randint(self.addlist['min'], self.addlist['max'])
                addt = self.addtopic(a, b)

                if addt and not (addt in additionlist):  # 算式是否生成？列表中是否有相同的算式，如果没有则添加到列表中。
                    additionlist.append(addt)
                    break

        return additionlist

    def subtracting(self):
        '''返回减法口算题'''

        slist = []
        for i in range(self.number):

            while (True):
                a = random.randint(self.subtractlist['min'], self.subtractlist['max'])
                b = random.randint(self.subtractlist['min'], self.subtractlist['max'])
                st = self.subtract(a, b)

                if st and not (st in slist):  # 算式是否生成？列表中是否有相同的算式，如果没有则添加到列表中。
                    slist.append(st)
                    break

        return slist

    def addtopic(self, a, b):
        '''根据两个数字返回一道口算加法题'''
        # 判断两个随机生成的数字不能相同， 不能为过滤列表中的数字，如果条件符合，即可生成算式
        if a != b and not (a in self.addlist['filter']) and not (b in self.addlist['filter']):
            if(self.carry == 0):#如果需要进位
                if(self.isCarry(a,b)):#判断是必须为进位
                    return "{}+{}=".format(a, b)
            elif(self.carry == 1):#如果需要不进位
                if(not self.isCarry(a, b)):  # 判断是必须为不进位
                    return "{}+{}=".format(a, b)
            elif(self.carry == 2):#随机的不论是否进位
                return "{}+{}=".format(a, b)
        else:
            return False

    def subtract(self, a, b):
        '''根据两个数字返回一道口算减法题'''
        # 判断两个随机生成的数字不能相同且a>b，不能为过滤列表中的数字，如果条件符合，即可生成算式
        if a > b and not (a in self.subtractlist['filter']) and not (b in self.subtractlist['filter']):
            if(self.abdication == 0):
                if(self.isAbdication(a,b)):
                    return "{}-{}=".format(a, b)
            elif(self.abdication == 1):
                if(not self.isAbdication(a,b)):
                    return "{}-{}=".format(a, b)
            elif(self.abdication == 2):
                return "{}-{}=".format(a, b)
        else:
            return False

    def getnum(self, number):
        '''反回一个整数的个位数'''
        value0 = number / 10
        value0 = int(value0)
        return number - value0 * 10

    def isCarry(self,a,b):
        '''判断加法是否存在进位'''
        if(self.getnum(a)+self.getnum(b) < 10):
            return False
        else:
            return True

    def isAbdication(self,a,b):
        '''判断减法是否存在退位'''
        if(self.getnum(b)>self.getnum(a)):
            return True
        else:
            return False

def main():
    '''程序入口'''
    print("程序开始！")
    psm = PrimarySchoolMathematics()
    print(psm.addition())
    print(psm.subtracting())


if __name__ == '__main__':
    main()  # 程序入口
