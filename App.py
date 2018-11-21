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

Author  : andywu1998
Mail    : 1078539713@qq.com


'''
import random,os,shutil
import tkinter as tk
from tkinter import messagebox  # 导入提示窗口包

from Psmrcddup import Generator
from PrintPreview import PrintPreview
from utils.PSM_help import *

__version__ = "0.2.0"



psm_list =[] #最终需要打印的所有口算题卷子
psm_type = []  #口算题详细配置参数
psm_title = []#口算卷子标题
psm_info = [] #卷内容提示语

app_title ="基于Python开发的小学生口算题生成器"
info_tit ="还没添加任何口算题到卷子中，请点击添加口算题按钮开始添加口算题！"#当前口算题卷子包含内容



def movdocx():
    '''负责把生成的口算题文件移动到指定目录'''
    docs = []#当前目录生成的文件列表
    print(os.path.dirname(os.path.abspath(__file__)))
    for p in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if p.endswith('.docx'):
            docs.append(p)
    # print(docs)
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docx')
    if os.path.isdir(p):
        shutil.rmtree(p)
        os.mkdir(p)
        for f in docs:
            shutil.move(f,p)
    else:
        os.mkdir(p)
        for f in docs:
            shutil.move(f,p)








def rdoprt():
    '''测试使用'''
    print('...')


def createPSM():
    '''创建口算题最终打印前的配置'''

    tmplist = eval(multistep1_entry.get())#获取运算项及运算结果范围设置

    multistep = [tmplist[0], tmplist[1], tmplist[2], tmplist[3], tmplist[4],]

    signum = ra1Var.get()#获取题类型设置
    step = rc1Var.get()#获取需要几步计算
    is_result = rd1Var.get() #题型设置

    is_bracket = multvar.get() #是否需要括号

    symbols = eval(multistep2_entry.get())
    number = sumVar.get()#获取需要生成的题数

    add = {"carry": add1Var.get(), }  # 加法设置
    sub = { "abdication": sub1Var.get(), }  # 减法设置
    mult = {}  # 乘法设置
    div = {}  # 除法设置


    # 组装
    tmp_type = [add, sub, mult, div, signum, step, number, is_result,is_bracket, multistep,symbols]


    #更新题库内容提示
    psm_type.append(tmp_type)
    if step == 1:

        if signum == 1:
            psm_info.append("加法口算题"+str(number)+"道")
            inofstr.set(psm_info)
        elif signum == 2:
            psm_info.append("减法口算题" + str(number) + "道")
            inofstr.set(psm_info)
        elif signum == 3:
            psm_info.append("乘法口算题" + str(number) + "道")
            inofstr.set(psm_info)
        elif signum == 4:
            psm_info.append("除法口算题" + str(number) + "道")
            inofstr.set(psm_info)
        else:
            raise Exception("没有这个题型哦")

    elif step == 2:
        psm_info.append("两步计算口算题" + str(number) + "道")
        inofstr.set(psm_info)

    elif step ==3:
        psm_info.append("三步计算口算题" + str(number) + "道")
        inofstr.set(psm_info)




def cleanPSM():
    '''清空当前口算题所有配置。'''
    global psm_info

    psm_type.clear()#清空配置表
    psm_info.clear()#清空内容提示
    inofstr.set((('')))#清空当前口算题卷子包含内容文本框
    psm_info.append(info_tit)
    inofstr.set(psm_info)
    psm_info.clear()#添加完毕后再次清空内容提示列表，如果重新添加口算题将重新添加list，防止list第一行为空


def producePSM():
    '''发布口算题保存.docx文件'''
    print(psm_type)#打印测试
    if len(psm_type) == 0:
        print('还没有添加口算题到列表中哈！')  # 打印测试
        messagebox.showinfo("提示", "还没有添加口算题到列表中哈！")
    else:
        #循环生成每套题
        for i in range(int(psm_entry.get())):
            templist = []
            for l in psm_type:
                g = Generator(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10])
                templist = templist + g.generate_data()
            random.shuffle(templist)
            print(templist)
            psm_list.append(templist)
        #为生成的文件起名
        psm_title.clear()
        for i in range(int(psm_entry.get())):
            psm_title.append(psmtitVar.get())
        print(psm_title)
        subtit = psmtit1Var.get()

        pp = PrintPreview(psm_list, psm_title,subtit, col=int(psmcol_entry.get()))
        pp.produce()#生成docx
        psm_list.clear()#清空打印列表。
        movdocx()
        messagebox.showinfo("成功提示","文件发布成功，保存在docx目录下，请查看！")





###########GUI布局############


root = tk.Tk()#创建一个root窗口
root.title(app_title)#设置窗口标题
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X,)

t_frame = tk.LabelFrame(top_frame, text="口算题类型选择及详细设置", padx=5, pady=5)
t_frame.pack(fill=tk.X, side=tk.TOP)

t1_frame = tk.LabelFrame(t_frame, text="运算项数值及结果范围设置及运算符号设置", padx=5, pady=5)
t1_frame.pack(fill=tk.X, side=tk.LEFT)

t2_frame = tk.LabelFrame(t_frame, text="选择几步口算", padx=5, pady=5)
t2_frame.pack(fill=tk.X, side=tk.LEFT)

t3_frame = tk.LabelFrame(t_frame, text="其它设置", padx=5, pady=5)
t3_frame.pack(fill=tk.X, side=tk.LEFT)

t4_frame = tk.LabelFrame(t_frame, text="题型设置", padx=5, pady=5)
t4_frame.pack(fill=tk.X, side=tk.LEFT)



c_frame = tk.LabelFrame(top_frame, text="加减乘除法详细设置", padx=5, pady=5)
c_frame.pack(fill=tk.X, side=tk.TOP)

multistep_frame = tk.LabelFrame(c_frame, text="多步运算题", padx=5, pady=5)
multistep_frame.pack(fill=tk.X, side=tk.TOP)

addattrs_frame = tk.LabelFrame(c_frame, text="加法", padx=5, pady=5)
addattrs_frame.pack(fill=tk.X, side=tk.TOP)

subattrs_frame = tk.LabelFrame(c_frame, text="减法", padx=5, pady=5)
subattrs_frame.pack(fill=tk.X, side=tk.TOP)


multattrs_frame = tk.LabelFrame(c_frame, text="乘除法", padx=5, pady=5)
multattrs_frame.pack(fill=tk.X, side=tk.TOP)






c1_frame = tk.LabelFrame(top_frame, text="添加口算题到卷子", padx=5, pady=5)
c1_frame.pack(fill=tk.X, side=tk.TOP)

add_btn = tk.Button(c1_frame, text="+++++++添加口算题+++++++",height=2,command=createPSM)
add_btn.pack(fill = tk.X,side=tk.TOP)

cle_btn = tk.Button(c1_frame, text="+++++++清空口算题+++++++",height=2,command=cleanPSM)
cle_btn.pack(fill = tk.X,side=tk.TOP)


b_frame = tk.LabelFrame(top_frame, text="当前口算题包含内容", padx=5, pady=5)
b_frame.pack(fill=tk.X, side=tk.TOP)

b1_frame = tk.LabelFrame(top_frame, text="打印试卷详细设置", padx=5, pady=5)
b1_frame.pack(fill=tk.X, side=tk.TOP)

b2_frame = tk.LabelFrame(top_frame, text="打印试卷详细设置", padx=5, pady=5)
b2_frame.pack(fill=tk.X, side=tk.TOP)

c_btn = tk.Button(top_frame, text="+++++++点此生成口算题打印文档+++++++",height=2,command=producePSM)
c_btn.pack(fill = tk.X,side=tk.TOP)

###########口算题类型选择############
ra1Var = tk.IntVar()
ra1=tk.Radiobutton(t1_frame,text='加法',value='1',variable=ra1Var,)
ra1.pack(anchor=tk.W,side=tk.LEFT)
ra2=tk.Radiobutton(t1_frame,text='减法',value='2',variable=ra1Var,)
ra2.pack(anchor=tk.W,side=tk.LEFT)
ra3=tk.Radiobutton(t1_frame,text='乘法',value='3',variable=ra1Var,)
ra3.pack(anchor=tk.W,side=tk.LEFT)
ra4=tk.Radiobutton(t1_frame,text='除法',value='4',variable=ra1Var,)
ra4.pack(anchor=tk.W,side=tk.LEFT)
ra1.select()



rc1Var = tk.IntVar()
rc1=tk.Radiobutton(t2_frame,text='单步',value='1',variable=rc1Var)
rc1.pack(anchor=tk.W,side=tk.LEFT)
rc2=tk.Radiobutton(t2_frame,text='两步',value='2',variable=rc1Var,)
rc2.pack(anchor=tk.W,side=tk.LEFT)
rc3=tk.Radiobutton(t2_frame,text='三步',value='3',variable=rc1Var,)
rc3.pack(anchor=tk.W,side=tk.LEFT)
rc1.select()


rd1Var = tk.IntVar()
rd1=tk.Radiobutton(t4_frame,text='求结果',value='0',variable=rd1Var)
rd1.pack(anchor=tk.W,side=tk.LEFT)
rc2=tk.Radiobutton(t4_frame,text='求算数项',value='1',variable=rd1Var,)
rc2.pack(anchor=tk.W,side=tk.LEFT)
rd1.select()


sumVar = tk.IntVar()
sumVar.set("20")
sum_label = tk.Label(t3_frame, text="生成数量:",font=("Symbol", 14))
sum_label.pack(side=tk.LEFT,fill=tk.X)
sum_entry = tk.Entry(t3_frame,width=8,textvariable=sumVar)
sum_entry.pack(fill=tk.X, side= tk.LEFT)

###########addattrs############




add1Var = tk.IntVar()
add1=tk.Radiobutton(addattrs_frame,text='随机进位',value='1',variable=add1Var,)
add1.pack(anchor=tk.W,side=tk.LEFT)
add2=tk.Radiobutton(addattrs_frame,text='加法进位',value='2',variable=add1Var,)
add2.pack(anchor=tk.W,side=tk.LEFT)
add3=tk.Radiobutton(addattrs_frame,text='没有进位',value='3',variable=add1Var,)
add3.pack(anchor=tk.W,side=tk.LEFT)
add1.select()




###########subattrs############






sub1Var = tk.IntVar()
sub1=tk.Radiobutton(subattrs_frame,text='随机退位',value='1',variable=sub1Var,)
sub1.pack(anchor=tk.W,side=tk.LEFT)
sub2=tk.Radiobutton(subattrs_frame,text='减法退位',value='2',variable=sub1Var,)
sub2.pack(anchor=tk.W,side=tk.LEFT)
sub3=tk.Radiobutton(subattrs_frame,text='没有退位',value='3',variable=sub1Var,)
sub3.pack(anchor=tk.W,side=tk.LEFT)
sub1.select()




###########multattrs divattrs############




mult1_label = tk.Label(multattrs_frame, text="乘除法暂无相关设置:",font=("Symbol", 14))
mult1_label.pack(side=tk.LEFT,fill=tk.X)
# mult1_entry = tk.Entry(multattrs_frame,width=8)
# mult1_entry.pack(fill=tk.X, side= tk.LEFT)
# mult1_entry.insert(0,'[1,81]')





###########divattrs############






###########multistep############


multistep1_label = tk.Label(multistep_frame, text="运算项及结果范围设置:",font=("Symbol", 14))
multistep1_label.pack(side=tk.LEFT,fill=tk.X)
multistep1_entry = tk.Entry(multistep_frame,width=34)
multistep1_entry.pack(fill=tk.X, side= tk.LEFT)
multistep1_entry.insert(0,'[[2,20],[2,20],[2,9],[2,9],[2,20]]')

multistep2_label = tk.Label(multistep_frame, text="运算符号设置:",font=("Symbol", 14))
multistep2_label.pack(side=tk.LEFT,fill=tk.X)
multistep2_entry = tk.Entry(multistep_frame,width=22)
multistep2_entry.pack(fill=tk.X, side= tk.LEFT)
multistep2_entry.insert(0,'[[1,2],[1,2],[1,2,3,4]]')


multvar = tk.IntVar()
multistep1=tk.Checkbutton(multistep_frame,text='使用括号', variable = multvar)
multistep1.pack(anchor=tk.W,side=tk.LEFT)




###########subattrs############



###########当前口算题卷子包含内容############
inofstr = tk.StringVar()
inofstr.set(info_tit)
inof_label = tk.Listbox(b_frame, listvariable=inofstr, height=6)
inof_label.pack(side=tk.TOP,fill=tk.X)


###########生成口算题卷############

psm_label = tk.Label(b1_frame, text="生成几套口算题:",font=("Symbol", 14))
psm_label.pack(side=tk.LEFT,fill=tk.X)
psm_entry = tk.Entry(b1_frame,width=6)
psm_entry.pack(fill=tk.X, side= tk.LEFT)
psm_entry.insert(0,'3')

psmcol_label = tk.Label(b1_frame, text="口算题列数:",font=("Symbol", 14))
psmcol_label.pack(side=tk.LEFT,fill=tk.X)
psmcol_entry = tk.Entry(b1_frame,width=6)
psmcol_entry.pack(fill=tk.X, side= tk.LEFT)
psmcol_entry.insert(0,'3')

psmtitVar = tk.StringVar()
psmtitVar.set("小学生口算题")
psmtit1Var = tk.StringVar()
psmtit1Var.set("姓名：__________ 日期：____月____日 时间：________ 对题：____道")
psmtit_label = tk.Label(b2_frame, text="口算题卷子标题:",font=("Symbol", 14))
psmtit_label.pack(side=tk.LEFT,fill=tk.X)
psmtit_entry = tk.Entry(b2_frame,width=30,textvariable=psmtitVar)
psmtit_entry.pack(fill=tk.X, side= tk.LEFT)
psmtit1_label = tk.Label(b2_frame, text="口算题卷子副标题:",font=("Symbol", 14))
psmtit1_label.pack(side=tk.LEFT,fill=tk.X)
psmtit1_entry = tk.Entry(b2_frame,width=30,textvariable=psmtit1Var)
psmtit1_entry.pack(fill=tk.X, side= tk.LEFT)



def main():
    print('程序开始运行')

    root.mainloop()



if __name__ == '__main__':
    main()
