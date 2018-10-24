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

加减法由于需要进位及退位的功能时，在一定数值范围内会产生口算题数量不够的情况，需要先判断范围内能够产生的合法口算题数目，如果当前需要生成的算数题大于实际生产出的口算题，
应该选择是否可以重复或是增加数值范围。

'''

import random


class PrimarySchoolMathematics:
    '''核心类，负责生成口算题。'''

    # 加法数字列表，最小数，最大数，需要的加法口算题总数，过滤掉的数字,是否可以生成相同的口算题,加法是否进位 是否进位：0进位1不进位2随机
    addlist = {'min': 0, 'max': 20, 'number': 20, 'filter': [0, 1], 'same': 1, 'carry': 0}

    # 减法数字列表，最小数，最大数，需要的加减法口算题总数,过滤掉的数字，是否可以生成相同的口算题,# 减法是否退位：0退位1不退位2随机
    subtractlist = {'min': 0, 'max': 20, 'number': 20, 'filter': [0, 10], 'same': 1, 'abdication': 0}

    def addition(self):
        '''返回加法口算题'''

        additionlist = []
        tmplist = []



        # 循环生成所有加法口算题
        for i in range(self.addlist['min'], self.addlist['max']):
            for j in range(self.addlist['min'], self.addlist['max']):
                addt = self.addtopic(i, j)
                if (addt):
                    additionlist.append(addt)
        print(len(additionlist))

        if (len(additionlist) >= self.addlist['number']):
            random.shuffle(additionlist)  # 洗牌，先打乱list中的排序
            tmplist = random.sample(additionlist, self.addlist['number'])  # 随机取需要的口算题量。
            return tmplist
        elif(len(additionlist) == 0):
            return '此数字范围内生成的加法口算题未能达到您要求的数目，请检查配置以适合程序的生成，请修改数值符合加法进位'
        else:
            if (self.addlist['same']):
                for i in range(self.addlist['number']):
                    k = random.randint(0, len(additionlist))
                    # print(k)
                    tmplist.append(additionlist[k - 1])

                return tmplist

            else:
                return '此数字范围内生成的加法口算题未能达到您要求的数目，请检查配置以适合程序的生成，比如设置可以生成相同的题'

    def subtracting(self):
        '''返回减法口算题'''

        slist = []
        tmplist = []


        # 循环生成所有减法口算题
        for i in range(self.addlist['min'], self.addlist['max']):
            for j in range(self.addlist['min'], self.addlist['max']):
                st = self.subtract(i, j)
                if (st):
                    slist.append(st)
        if (len(slist) >= self.subtractlist['number']):
            random.shuffle(slist)  # 洗牌，先打乱list中的排序
            tmplist = random.sample(slist, self.subtractlist['number'])  # 随机取需要的口算题量。
            return tmplist
        elif(len(slist) == 0):
            return '此数字范围内生成的减法口算题未能达到您要求的数目，请检查配置以适合程序的生成，请修改数值符合减法退位'
        else:
            if (self.subtractlist['same']):
                for i in range(self.subtractlist['number']):
                    k = random.randint(0, len(slist))
                    tmplist.append(slist[k - 1])
                return tmplist
            else:
                return '此数字范围内生成的减法口算题未能达到您要求的数目，请检查配置以适合程序的生成，比如设置可以生成相同的题'

    def addtopic(self, a, b):
        '''根据两个数字返回一道单步口算加法题'''
        # 判断两个随机生成的数字不能相同， 不能为过滤列表中的数字，如果条件符合，即可生成算式
        if a != b and not (a in self.addlist['filter']) and not (b in self.addlist['filter']):
            if (self.addlist['carry'] == 0):  # 如果需要进位
                if (self.isCarry(a, b)):  # 判断是必须为进位
                    return "{}+{}=".format(a, b)
            elif (self.addlist['carry'] == 1):  # 如果需要不进位subtractlist['abdication']
                if (not self.isCarry(a, b)):  # 判断是必须为不进位
                    return "{}+{}=".format(a, b)
            elif (self.addlist['carry'] == 2):  # 随机的不论是否进位
                return "{}+{}=".format(a, b)
        else:
            return False



    def subtract(self, a, b):
        '''根据两个数字返回一道单步口算减法题'''
        # 判断两个随机生成的数字不能相同且a>b，不能为过滤列表中的数字，如果条件符合，即可生成算式
        if a > b and not (a in self.subtractlist['filter']) and not (b in self.subtractlist['filter']):
            if (self.subtractlist['abdication'] == 0):
                if (self.isAbdication(a, b)):
                    return "{}-{}=".format(a, b)
            elif (self.subtractlist['abdication'] == 1):
                if (not self.isAbdication(a, b)):
                    return "{}-{}=".format(a, b)
            elif (self.subtractlist['abdication'] == 2):
                return "{}-{}=".format(a, b)
        else:
            return False




    def getnum(self, number):
        '''反回一个整数的个位数'''
        value0 = number / 10
        value0 = int(value0)
        return number - value0 * 10

    def isCarry(self, a, b):
        '''判断加法是否存在进位'''
        if (self.getnum(a) + self.getnum(b) < 10):
            return False
        else:
            return True

    def isAbdication(self, a, b):
        '''判断减法是否存在退位'''
        if (self.getnum(b) > self.getnum(a)):
            return True
        else:
            return False

    def printMathematics(self):
        plist = []
        if(self.addlist['number']>0):
            plist=plist+self.addition()

        if(self.subtractlist['number']>0):
            plist = plist+self.subtracting()

        if(len(plist)==0):
            print('不需要设置一下口算题的数目吗？')

            str = ''
        print(plist)

def main():
    '''程序入口'''
    print("程序开始！")
    psm = PrimarySchoolMathematics()
    print(psm.addition())
    print(psm.subtracting())
    psm.printMathematics()


if __name__ == '__main__':
    main()  # 程序入口
