#!/usr/bin/env python3
# -*- coding=utf-8 -*-

'''

临时程序入口
后续会写一个类，用来配置口算题生成前的配置，然后配以GUI实现可视化配置。

'''
import random
import tkinter as tk
from tkinter import ttk

from Psmrcddup import Generator
from PrintPreview import PrintPreview







def cdef():
    if var.get():
        strvar.set("看，我改变了！")
    else:
        strvar.set("有种你点我试试")


def rdoprt():
    print('...')





def go(*args):   #处理事件，*args表示可变参数
        print(comboxlist.get()) #打印选中的值



root = tk.Tk()#创建一个root窗口
root.title('基于Python开发的小学生口算题生成器')#设置窗口标题
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X,)


t_frame = tk.LabelFrame(top_frame, text="口算题类型选择", padx=5, pady=5)
t_frame.pack(fill=tk.X, side=tk.TOP)


c_frame = tk.LabelFrame(top_frame, text="口算题详细设置", padx=5, pady=5)
c_frame.pack(fill=tk.X, side=tk.TOP)

l_frame = tk.LabelFrame(c_frame, text="进退位设置", padx=5, pady=5)
l_frame.pack(fill=tk.X, side=tk.TOP)




###########口算题类型选择############
vara = tk.StringVar()
vara.set("L")  # initialize
ra1=tk.Radiobutton(t_frame,text='加法',variable=vara,value='1',command=rdoprt)
ra1.pack(anchor=tk.W,side=tk.LEFT)
ra2=tk.Radiobutton(t_frame,text='减法',variable=vara,value='2',command=rdoprt)
ra2.pack(anchor=tk.W,side=tk.LEFT)
ra3=tk.Radiobutton(t_frame,text='乘法',variable=vara,value='3',command=rdoprt)
ra3.pack(anchor=tk.W,side=tk.LEFT)
ra4=tk.Radiobutton(t_frame,text='除法',variable=vara,value='4',command=rdoprt)
ra4.pack(anchor=tk.W,side=tk.LEFT)
ra1.select()



###########口算题类型选择############
varb = tk.StringVar()
varb.set("L")  # initialize
rb1=tk.Radiobutton(l_frame,text='随机',variable=varb,value='1',command=rdoprt)
rb1.pack(anchor=tk.W,side=tk.LEFT)
rb2=tk.Radiobutton(l_frame,text='加法进位',variable=varb,value='2',command=rdoprt)
rb2.pack(anchor=tk.W,side=tk.LEFT)
rb3=tk.Radiobutton(l_frame,text='加法无进位',variable=varb,value='3',command=rdoprt)
rb3.pack(anchor=tk.W,side=tk.LEFT)
rb4=tk.Radiobutton(l_frame,text='减法退位',variable=varb,value='4',command=rdoprt)
rb4.pack(anchor=tk.W,side=tk.LEFT)
rb5=tk.Radiobutton(l_frame,text='减法无退位',variable=varb,value='5',command=rdoprt)
rb5.pack(anchor=tk.W,side=tk.LEFT)
rb1.select()










def main():
    print('程序开始运行')
    root.mainloop()
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
    # - @num int
    #     需要生成的题数量
    #     默认：80

    # 配置每套题包括的内容，至少有一种题型，每套题的总数量为几种题型的数量总合。
    psm_type = [
        [1, (0, 20), 2, 1, (0, 1), True, False, 25],
        [2, (0, 20), 3, 1, (0, 1), True, False, 25],
        [3, (0, 9), 1, 1, (0,), True, False, 25],
        [4, (0, 81), 1, 1, (0, 1), True, False, 25]
    ]

    #循环生成每套题
    for i in range(sets):
        templist = []
        for l in psm_type:
            g = Generator(signum=l[0], range=l[1], need_carry=l[2], step=l[3], filter=l[4], same=l[5],num=l[7])
            templist = templist + g.generate_data()
        random.shuffle(templist)
        print(templist)
        psm_list.append(templist)
    #这里的标题后继需要进行判断进行起名，暂时固定
    pp = PrintPreview(psm_list, ['小学生口算题','小学生口算题','小学生口算题'], 4)
    pp.produce()#生成docx


if __name__ == '__main__':
    main()
