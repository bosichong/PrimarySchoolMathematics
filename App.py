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


'''
import random,os,shutil
import tkinter as tk
from tkinter import messagebox  # 导入提示窗口包

from Psmrcddup import Generator
from PrintPreview import PrintPreview

__version__ = "0.1.1"



psm_list =[] #最终需要打印的所有口算题卷子
psm_type = []  #口算题详细配置参数
psm_title = []#口算卷子标题
psm_info = [] #卷内容提示语

app_title ="基于Python开发的小学生口算题生成器"
info_tit ="还没添加任何口算题到卷子中，请点击添加口算题按钮开始添加口算题！"#当前口算题卷子包含内容


def movdocx():
    '''负责把生成的口算题文件移动到指定目录'''
    docs = []#当前目录生成的文件列表
    for p in os.listdir(os.path.dirname(__file__)):
        if p.endswith('.docx'):
            docs.append(p)
    # print(docs)
    p = os.path.join(os.path.dirname(__file__), 'docx')
    if os.path.isdir(p):
        shutil.rmtree(p)
        os.mkdir(p)
        for f in docs:
            shutil.move(f,p)
    else:
        os.mkdir(p)
        for f in docs:
            shutil.move(f,p)


def filterPSM():
    '''当选择加减乘除法的时候，用来屏蔽掉不能使用的进退位选择'''
    if ra1Var.get() == 1:
        if rb1Var.get() == 3:
            messagebox.showinfo("提示", "加法没有退位，请重新选择！")
            rb1.select()
    elif ra1Var.get() == 2:
        if rb1Var.get() == 2:
            messagebox.showinfo("提示", "减法没有进位，请重新选择！")
            rb1.select()
    elif ra1Var.get() == 3 or ra1Var.get() == 4:
        if rb1Var.get() == 2 or rb1Var.get() == 3 or rb1Var.get() == 4 :
            messagebox.showinfo("提示", "乘除法无法选择进退位，只能随机！")
            rb1.select()







def rdoprt():
    '''测试使用'''
    print('...')


def createPSM():
    '''创建口算题最终打印前的配置'''

    tmp_signum = ra1Var.get()#获取题类型设置
    tmp_step = rc1Var.get()#获取需要几步计算
    tmp_range = (int(min_entry.get()),int(add2_entry.get()))#获取数值取值范围
    tmp_same = sameVar.get()#获取题是否可以相同的设置
    tmp_carry = rb1Var.get()#获取是否需要进退位
    tmp_filter = eval('('+filter_entry.get()+')')#获取过滤数字
    tmp_num = sumVar.get()#获取需要生成的题数

    # 组装
    tmp_type = [tmp_signum,tmp_range,tmp_carry,tmp_step,tmp_filter,tmp_same,tmp_num]


    #更新题库内容提示
    psm_type.append(tmp_type)
    if tmp_signum == 1:
        psm_info.append("加法口算题"+str(tmp_num)+"道")
        inofstr.set(psm_info)
    elif tmp_signum == 2:
        psm_info.append("减法口算题" + str(tmp_num) + "道")
        inofstr.set(psm_info)
    elif tmp_signum == 3:
        psm_info.append("乘法口算题" + str(tmp_num) + "道")
        inofstr.set(psm_info)
    elif tmp_signum == 4:
        psm_info.append("除法口算题" + str(tmp_num) + "道")
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
                g = Generator(signum=l[0], range=l[1], need_carry=l[2], step=l[3], filter=l[4], same=l[5],num=l[6])
                templist = templist + g.generate_data()
            random.shuffle(templist)
            print(templist)
            psm_list.append(templist)
        #为生成的文件起名
        psm_title.clear()
        for i in range(int(psm_entry.get())):
            psm_title.append(psmtitVar.get())
        print(psm_title)

        pp = PrintPreview(psm_list, psm_title, col=int(psmcol_entry.get()))
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

t1_frame = tk.LabelFrame(t_frame, text="加减乘除选择", padx=5, pady=5)
t1_frame.pack(fill=tk.X, side=tk.LEFT)

t2_frame = tk.LabelFrame(t_frame, text="选择几步口算", padx=5, pady=5)
t2_frame.pack(fill=tk.X, side=tk.LEFT)

t3_frame = tk.LabelFrame(t_frame, text="其它设置", padx=5, pady=5)
t3_frame.pack(fill=tk.X, side=tk.LEFT)



c_frame = tk.LabelFrame(top_frame, text="加减乘除法详细设置", padx=5, pady=5)
c_frame.pack(fill=tk.X, side=tk.TOP)

addattrs_frame = tk.LabelFrame(c_frame, text="加法", padx=5, pady=5)
addattrs_frame.pack(fill=tk.X, side=tk.TOP)

subattrs_frame = tk.LabelFrame(c_frame, text="减法", padx=5, pady=5)
subattrs_frame.pack(fill=tk.X, side=tk.TOP)


multattrs_frame = tk.LabelFrame(c_frame, text="乘法", padx=5, pady=5)
multattrs_frame.pack(fill=tk.X, side=tk.TOP)

divattrs_frame = tk.LabelFrame(c_frame, text="除法", padx=5, pady=5)
divattrs_frame.pack(fill=tk.X, side=tk.TOP)

multistep_frame = tk.LabelFrame(c_frame, text="多步运算题", padx=5, pady=5)
multistep_frame.pack(fill=tk.X, side=tk.TOP)



c1_frame = tk.LabelFrame(top_frame, text="添加口算题到卷子", padx=5, pady=5)
c1_frame.pack(fill=tk.X, side=tk.TOP)

add_btn = tk.Button(c1_frame, text="+++++++添加口算题+++++++",height=2,command=createPSM)
add_btn.pack(fill = tk.X,side=tk.TOP)

cle_btn = tk.Button(c1_frame, text="+++++++清空口算题+++++++",height=2,command=cleanPSM)
cle_btn.pack(fill = tk.X,side=tk.TOP)


b_frame = tk.LabelFrame(top_frame, text="当前口算题包含内容", padx=5, pady=5)
b_frame.pack(fill=tk.X, side=tk.TOP)

b1_frame = tk.LabelFrame(top_frame, text="请真写需要生成多少套需要打印的试卷", padx=5, pady=5)
b1_frame.pack(fill=tk.X, side=tk.TOP)

c_btn = tk.Button(top_frame, text="+++++++点此生成口算题打印文档+++++++",height=2,command=producePSM)
c_btn.pack(fill = tk.X,side=tk.TOP)

###########口算题类型选择############
ra1Var = tk.IntVar()
ra1=tk.Radiobutton(t1_frame,text='加法',value='1',variable=ra1Var,command=filterPSM)
ra1.pack(anchor=tk.W,side=tk.LEFT)
ra2=tk.Radiobutton(t1_frame,text='减法',value='2',variable=ra1Var,command=filterPSM)
ra2.pack(anchor=tk.W,side=tk.LEFT)
ra3=tk.Radiobutton(t1_frame,text='乘法',value='3',variable=ra1Var,command=filterPSM)
ra3.pack(anchor=tk.W,side=tk.LEFT)
ra4=tk.Radiobutton(t1_frame,text='除法',value='4',variable=ra1Var,command=filterPSM)
ra4.pack(anchor=tk.W,side=tk.LEFT)
ra1.select()



rc1Var = tk.IntVar()
rc1=tk.Radiobutton(t2_frame,text='单步',value='1',variable=rc1Var)
rc1.pack(anchor=tk.W,side=tk.LEFT)
rc2=tk.Radiobutton(t2_frame,text='两步',value='2',variable=rc1Var,state=tk.DISABLED)
rc2.pack(anchor=tk.W,side=tk.LEFT)
rc3=tk.Radiobutton(t2_frame,text='三步',value='3',variable=rc1Var,state=tk.DISABLED)
rc3.pack(anchor=tk.W,side=tk.LEFT)
rc1.select()



sumVar = tk.IntVar()
sumVar.set("20")
sum_label = tk.Label(t3_frame, text="生成数量:",font=("Symbol", 14))
sum_label.pack(side=tk.LEFT,fill=tk.X)
sum_entry = tk.Entry(t3_frame,width=8,textvariable=sumVar)
sum_entry.pack(fill=tk.X, side= tk.LEFT)

###########addattrs############




add2_label = tk.Label(addattrs_frame, text="运算结果范围:",font=("Symbol", 14))
add2_label.pack(side=tk.LEFT,fill=tk.X)
add2_entry = tk.Entry(addattrs_frame,width=8)
add2_entry.pack(fill=tk.X, side= tk.LEFT)
add2_entry.insert(0,'[1,20]')



add1Var = tk.IntVar()
add1=tk.Radiobutton(addattrs_frame,text='随机进位',value='1',variable=add1Var,command=filterPSM)
add1.pack(anchor=tk.W,side=tk.LEFT)
add2=tk.Radiobutton(addattrs_frame,text='加法进位',value='2',variable=add1Var,command=filterPSM)
add2.pack(anchor=tk.W,side=tk.LEFT)
add3=tk.Radiobutton(addattrs_frame,text='没有进位',value='3',variable=add1Var,command=filterPSM)
add3.pack(anchor=tk.W,side=tk.LEFT)
add1.select()




###########subattrs############




sub1_label = tk.Label(subattrs_frame, text="运算结果范围:",font=("Symbol", 14))
sub1_label.pack(side=tk.LEFT,fill=tk.X)
sub1_entry = tk.Entry(subattrs_frame,width=8)
sub1_entry.pack(fill=tk.X, side= tk.LEFT)
sub1_entry.insert(0,'[1,19]')

sub1Var = tk.IntVar()
sub1=tk.Radiobutton(subattrs_frame,text='随机退位',value='1',variable=sub1Var,command=filterPSM)
sub1.pack(anchor=tk.W,side=tk.LEFT)
sub2=tk.Radiobutton(subattrs_frame,text='减法退位',value='2',variable=sub1Var,command=filterPSM)
sub2.pack(anchor=tk.W,side=tk.LEFT)
sub3=tk.Radiobutton(subattrs_frame,text='没有退位',value='3',variable=sub1Var,command=filterPSM)
sub3.pack(anchor=tk.W,side=tk.LEFT)
sub1.select()




###########multattrs############




mult1_label = tk.Label(multattrs_frame, text="运算结果范围:",font=("Symbol", 14))
mult1_label.pack(side=tk.LEFT,fill=tk.X)
mult1_entry = tk.Entry(multattrs_frame,width=8)
mult1_entry.pack(fill=tk.X, side= tk.LEFT)
mult1_entry.insert(0,'[1,81]')





###########divattrs############



div1_label = tk.Label(divattrs_frame, text="运算结果范围:",font=("Symbol", 14))
div1_label.pack(side=tk.LEFT,fill=tk.X)
div1_entry = tk.Entry(divattrs_frame,width=8)
div1_entry.pack(fill=tk.X, side= tk.LEFT)
div1_entry.insert(0,'[1,9]')




###########multistep############


multistep1_label = tk.Label(multistep_frame, text="运算项数值范围:",font=("Symbol", 14))
multistep1_label.pack(side=tk.LEFT,fill=tk.X)
multistep1_entry = tk.Entry(multistep_frame,width=34)
multistep1_entry.pack(fill=tk.X, side= tk.LEFT)
multistep1_entry.insert(0,'[[1,9],[1,9],[1,9],[1,9]]')

multistep2_label = tk.Label(multistep_frame, text="运算符号设置:",font=("Symbol", 14))
multistep2_label.pack(side=tk.LEFT,fill=tk.X)
multistep2_entry = tk.Entry(multistep_frame,width=22)
multistep2_entry.pack(fill=tk.X, side= tk.LEFT)
multistep2_entry.insert(0,'[[1,2,3],[1,2,3],[1,2],[1,2]]')



multistep1=tk.Checkbutton(multistep_frame,text='使用括号',command=filterPSM)
multistep1.pack(anchor=tk.W,side=tk.LEFT)




###########subattrs############



###########当前口算题卷子包含内容############
inofstr = tk.StringVar()
inofstr.set(info_tit)
inof_label = tk.Listbox(b_frame, listvariable=inofstr,)
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
psmtit_label = tk.Label(b1_frame, text="口算题卷子标题:",font=("Symbol", 14))
psmtit_label.pack(side=tk.LEFT,fill=tk.X)
psmtit_entry = tk.Entry(b1_frame,width=30,textvariable=psmtitVar)
psmtit_entry.pack(fill=tk.X, side= tk.LEFT)



def main():
    print('程序开始运行')

    root.mainloop()



if __name__ == '__main__':
    main()
