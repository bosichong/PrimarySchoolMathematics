#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-11-02
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 基于Python开发的小学生口算题生成器
# @Url     : http://2vv.net/blog/83.html
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


特别感谢一下二位的鼎力支持！

Author  : rcddup
Mail    : 410093793@qq.com

Author  : andywu1998
Mail    : 1078539713@qq.com


'''

import wx
import os
import shutil
import random
from Psmrcddup import Generator
from PrintPreview import PrintPreview
from APPconfig import AppConfig


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.multistep = [[1, 20], [1, 20], [
            1, 20], [1, 20], [1, 20]]  # 默认算数项值
        self.symbols = [[1, 2], [1, 2], [1, 2]]  # 默认运算符号值
        self.psm_list = []  # 最终需要打印的所有口算题卷子
        self.psm_type = []  # 口算题详细配置参数
        self.psm_title = []  # 口算卷子标题
        self.psm_info = ""  # 卷内容提示语
        self.config = AppConfig()  # 程序配置文件对象

        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, u"运算类型选择", choices=[u"加法", u"减法", u"乘法", u"除法"],
                                       majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_2 = wx.RadioBox(self, wx.ID_ANY, u"选择几步运算", choices=[u"一步", u"二步", u"三步"], majorDimension=1,
                                       style=wx.RA_SPECIFY_ROWS)
        self.radio_box_3 = wx.RadioBox(self, wx.ID_ANY, u"题型设置", choices=[u"求结果", u"求算数项"], majorDimension=1,
                                       style=wx.RA_SPECIFY_ROWS)
        self.button_1 = wx.Button(self, wx.ID_ANY, u"运算项及结果范围设置")
        self.button_1.Bind(wx.EVT_BUTTON, self.onRET1)
        self.button_2 = wx.Button(self, wx.ID_ANY, u"运算符号设置")
        self.button_2.Bind(wx.EVT_BUTTON, self.onRET2)
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, u"使用括号")
        self.radio_box_4 = wx.RadioBox(self, wx.ID_ANY, u"加法设置", choices=[u"随机进位", u"加法进位", u"没有进位"], majorDimension=1,
                                       style=wx.RA_SPECIFY_ROWS)
        self.radio_box_5 = wx.RadioBox(self, wx.ID_ANY, u"减法设置", choices=[u"随机退位", u"减法退位", u"没有退位"], majorDimension=1,
                                       style=wx.RA_SPECIFY_ROWS)
        self.text_ctrl_16 = wx.TextCtrl(
            self, wx.ID_ANY, "20", style=wx.TE_CENTRE)
        self.button_6 = wx.Button(self, wx.ID_ANY, u"添加口算题")

        self.button_7 = wx.Button(self, wx.ID_ANY, u"清空口算题")

        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_2 = wx.TextCtrl(
            self, wx.ID_ANY, "5", style=wx.TE_CENTRE)
        self.text_ctrl_3 = wx.TextCtrl(
            self, wx.ID_ANY, "3", style=wx.TE_CENTRE)
        self.button_3 = wx.Button(self, wx.ID_ANY, u"设置口算卷子保存目录")
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, u"小学生口算题")
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, u"姓名：__________ 日期：____月____日 时间：________ 对题：____道",
                                       style=wx.TE_LEFT)
        self.button_8 = wx.Button(self, wx.ID_ANY, u"点此生成口算题打印文档")

        self.app_title = "基于Python开发的小学生口算题生成器"
        self.info_tit = "还没添加任何口算题到卷子中，请点击添加口算题按钮开始添加口算题！"  # 当前口算题卷子包含内容

        self.__set_properties()
        self.__do_layout()

        self.button_6.Bind(wx.EVT_BUTTON, self.createPSM)
        self.button_7.Bind(wx.EVT_BUTTON, self.cleanPSM)
        self.button_3.Bind(wx.EVT_BUTTON, self.save_PSM_dir)
        self.button_8.Bind(wx.EVT_BUTTON, self.producePSM)

        self.radio_box_1.Bind(wx.EVT_RADIOBOX, self.saveSignum)
        self.radio_box_2.Bind(wx.EVT_RADIOBOX, self.saveStep)
        self.radio_box_3.Bind(wx.EVT_RADIOBOX, self.saveIs_Result)
        self.radio_box_4.Bind(wx.EVT_RADIOBOX, self.saveAdd)
        self.radio_box_5.Bind(wx.EVT_RADIOBOX, self.saveSub)

        self.checkbox_1.Bind(wx.EVT_CHECKBOX, self.saveIs_Bracket)

        self.text_ctrl_2.Bind(wx.EVT_TEXT, self.saveJuanzishu)
        self.text_ctrl_3.Bind(wx.EVT_TEXT, self.saveLieshu)
        self.text_ctrl_4.Bind(wx.EVT_TEXT, self.saveJz_title)
        self.text_ctrl_5.Bind(wx.EVT_TEXT, self.saveInf_title)
        self.text_ctrl_16.Bind(wx.EVT_TEXT, self.saveNumber)

        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(self.app_title)
        self.radio_box_1.SetSelection(
            int(self.config.c.get('config', 'signum')) - 1)
        self.radio_box_2.SetSelection(
            int(self.config.c.get('config', 'step')) - 1)
        self.radio_box_3.SetSelection(
            int(self.config.c.get('config', 'is_result')))
        self.radio_box_4.SetSelection(
            int(self.config.c.get('addattrs', 'carry')) - 1)
        self.radio_box_5.SetSelection(
            int(self.config.c.get('subattrs', 'abdication')) - 1)
        self.checkbox_1.SetValue(
            int(self.config.c.get('config', 'is_bracket')))
        self.text_ctrl_16.SetValue(self.config.c.get('config', 'number'))
        self.text_ctrl_2.SetValue(self.config.c.get('config', 'juanzishu'))
        self.text_ctrl_3.SetValue(self.config.c.get('config', 'lieshu'))
        self.text_ctrl_4.SetValue(self.config.c.get('config', 'jz_title'))
        self.text_ctrl_5.SetValue(self.config.c.get('config', 'inf_title'))
        self.button_6.SetMinSize((160, 22))
        self.button_7.SetMinSize((160, 22))
        self.text_ctrl_1.SetMinSize((100, 40))

        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"卷子大标题小标题设置"), wx.HORIZONTAL)
        sizer_13 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"口算卷设置"), wx.HORIZONTAL)
        sizer_12 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"当前口算题包含内容"), wx.HORIZONTAL)
        sizer_11 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"添加口算题到卷子"), wx.VERTICAL)
        sizer_22 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"详细设置"), wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"运算项结果符号设置"), wx.HORIZONTAL)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"口算题类型选择"), wx.HORIZONTAL)
        sizer_2.Add(self.radio_box_1, 0, 0, 0)
        sizer_2.Add(self.radio_box_2, 0, 0, 0)
        sizer_2.Add(self.radio_box_3, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 1)
        sizer_5.Add(self.button_1, 0, 0, 0)
        sizer_5.Add(self.button_2, 0, 0, 0)
        sizer_5.Add(self.checkbox_1, 0, 0, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_24.Add(self.radio_box_4, 0, 0, 0)
        sizer_24.Add(self.radio_box_5, 0, 0, 0)
        sizer_4.Add(sizer_24, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 0, wx.ALL | wx.EXPAND, 1)
        label_17 = wx.StaticText(self, wx.ID_ANY, u"口算题数：")
        sizer_22.Add(label_17, 0, 0, 0)
        sizer_22.Add(self.text_ctrl_16, 0, 0, 0)
        sizer_23.Add(self.button_6, 0, wx.ALL | wx.EXPAND, 0)
        sizer_23.Add(self.button_7, 0, wx.ALL | wx.EXPAND, 0)
        sizer_22.Add(sizer_23, 1, wx.EXPAND, 0)
        sizer_11.Add(sizer_22, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_11, 0, wx.ALL | wx.EXPAND, 1)
        sizer_12.Add(self.text_ctrl_1, 1, wx.ALL | wx.EXPAND, 0)
        sizer_1.Add(sizer_12, 1, wx.ALL | wx.EXPAND, 1)
        label_2 = wx.StaticText(self, wx.ID_ANY, u"生成卷子数量：")
        sizer_13.Add(label_2, 0, 0, 0)
        sizer_13.Add(self.text_ctrl_2, 0, wx.LEFT, 8)
        label_3 = wx.StaticText(self, wx.ID_ANY, u"口算题列数：")
        sizer_13.Add(label_3, 0, 0, 0)
        sizer_13.Add(self.text_ctrl_3, 0, 0, 0)
        sizer_13.Add(self.button_3, 0, 0, 0)
        sizer_1.Add(sizer_13, 0, wx.ALL | wx.EXPAND, 1)
        label_4 = wx.StaticText(self, wx.ID_ANY, u"卷子标题：")
        sizer_14.Add(label_4, 0, 0, 0)
        sizer_14.Add(self.text_ctrl_4, 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, u"卷子副标题：")
        sizer_14.Add(label_5, 0, 0, 0)
        sizer_14.Add(self.text_ctrl_5, 1, wx.ALL, 0)
        sizer_1.Add(sizer_14, 0, wx.ALL | wx.EXPAND, 1)
        sizer_1.Add(self.button_8, 0, wx.ALL | wx.EXPAND, 1)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def onRET1(self, e):
        '''点击弹出算数项及结果设置Dialog'''
        myDialog = MyDialog(self, wx.ID_ANY, pos=(300, 300))
        myDialog.ShowModal()
        if myDialog.ret:
            self.multistep = myDialog.retdata  # 取得算数项设置的返回结果
            print(self.multistep)
            self.config.saveMultistep(str(myDialog.retdata))

    def onRET2(self, e):
        '''点击弹出算数项及结果设置Dialog'''
        myDialog1 = MyDialog1(self, wx.ID_ANY, pos=(300, 300))
        myDialog1.ShowModal()
        if myDialog1.ret:
            self.symbols = myDialog1.retdata  # 取得算数项设置的返回结果
            print(self.symbols)
            self.config.saveSymbols(str(myDialog1.retdata))

    def movdocx(self):
        '''负责把生成的口算题文件移动到指定目录
        默认把口算题移动到'项目/docx/'下，其他目录需要指定。

        '''
        docs = []  # 当前目录生成的文件列表
        print(os.path.dirname(os.path.abspath(__file__)))
        for p in os.listdir(os.path.dirname(os.path.abspath(__file__))):
            if p.endswith('.docx'):
                docs.append(p)
        # print(docs)
        # p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docx')
        p = os.path.join(self.config.c.get('config','docx'), 'docx')#最后保存目录设置，保存在当前目录下的docx目录下
        if os.path.isdir(p):
            shutil.rmtree(p)
            os.mkdir(p)
            for f in docs:
                shutil.move(f, p)
        else:
            os.mkdir(p)
            for f in docs:
                shutil.move(f, p)

    def createPSM(self, e):
        '''创建口算题最终打印前的配置'''
        self.config.readINI()

        signum = int(self.config.c.get('config', 'signum'))
        step = int(self.config.c.get('config', 'step'))
        number = int(self.config.c.get('config', 'number'))

        # 组装
        tmp_type = self.config.loadINI()  # 加载

        if step == 1 and signum == 4:
            if self.multistep[1][0] <= 0:
                wx.MessageBox('除法时余数不能为0，请修改算数项设置', '错误提示',
                              wx.OK | wx.ICON_ERROR)
                return 0
        # 多步运算时除法余数为零判断
        if step > 1:
            print(4 in self.symbols[0] and self.multistep[1][0] <= 0)
            if (4 in self.symbols[0] and self.multistep[1][0] <= 0) or (
                    4 in self.symbols[1] and self.multistep[2][0] <= 0) or (
                    4 in self.symbols[2] and self.multistep[3][0] <= 0):
                wx.MessageBox('除法时余数不能为0，请修改算数项设置', '错误提示',
                              wx.OK | wx.ICON_ERROR)

        # 更新题库内容提示
        self.psm_type.append(tmp_type)
        if step == 1:

            if signum == 1:
                self.psm_info = self.psm_info + "加法口算题" + str(number) + "道|||"
                print(self.psm_info)
                self.text_ctrl_1.SetValue(self.psm_info)
            elif signum == 2:
                self.psm_info = self.psm_info + "减法口算题" + str(number) + "道|||"
                self.text_ctrl_1.SetValue(self.psm_info)
            elif signum == 3:
                self.psm_info = self.psm_info + "乘法口算题" + str(number) + "道|||"
                self.text_ctrl_1.SetValue(self.psm_info)
            elif signum == 4:
                self.psm_info = self.psm_info + "除法口算题" + str(number) + "道|||"
                self.text_ctrl_1.SetValue(self.psm_info)
            else:
                raise Exception("没有这个题型哦")

        elif step == 2:
            self.psm_info = self.psm_info + "两步计算口算题" + str(number) + "道|||"
            self.text_ctrl_1.SetValue(self.psm_info)

        elif step == 3:
            self.psm_info = self.psm_info + "三步计算口算题" + str(number) + "道|||"
            self.text_ctrl_1.SetValue(self.psm_info)

    def cleanPSM(self, e):
        '''清空当前口算题所有配置。'''

        self.psm_type.clear()  # 清空配置表
        self.psm_info = ""  # 清空内容提示
        self.text_ctrl_1.SetValue("")  # 清空当前口算题卷子包含内容文本框
        self.psm_info = self.info_tit
        self.text_ctrl_1.SetValue(self.psm_info)
        self.psm_info = ""  # 添加完毕后再次清空内容提示列表，如果重新添加口算题将重新添加list，防止list第一行为空

    def producePSM(self, e):
        '''发布口算题保存.docx文件'''
        # print(self.psm_type)  # 打印测试
        if len(self.psm_type) == 0:
            print('还没有添加口算题到列表中哈！')  # 打印测试
            wx.MessageBox('还没有添加口算题到列表中哈！', '提示',
                          wx.OK | wx.ICON_INFORMATION)
        else:
            # 循环生成每套题

            for i in range(int(self.text_ctrl_2.GetValue())):
                templist = []
                for l in self.psm_type:
                    print(l)
                    g = Generator(l[0], l[1], l[2], l[3], l[4],
                                  l[5], l[6], l[7], l[8], l[9], l[10])
                    templist = templist + g.generate_data()
                random.shuffle(templist)
                print(templist)
                self.psm_list.append(templist)
                # 为生成的文件起名r
                self.psm_title.clear()

            for i in range(int(self.text_ctrl_2.GetValue())):
                self.psm_title.append(self.text_ctrl_4.GetValue())
            # print(self.psm_title)
            subtit = self.text_ctrl_5.GetValue()

            pp = PrintPreview(self.psm_list, self.psm_title,
                              subtit, col=int(self.text_ctrl_3.GetValue()))
            pp.produce()  # 生成docx
            self.psm_list.clear()  # 清空打印列表。
            self.movdocx()
            wx.MessageBox('文件发布成功，保存在'+self.config.c.get('config','docx')+os.sep+'docx 目录下，请查看！！', '成功提示',
                          wx.OK | wx.ICON_INFORMATION)

    def saveSignum(self, e):
        '''保存题型设置'''
        rb = e.GetEventObject()
        # print(rb.GetSelection(), rb.GetStringSelection())  # 打印当前单选按钮的选项
        self.config.saveSignum('{0}'.format(rb.GetSelection() + 1))

    def saveStep(self, e):
        rb = e.GetEventObject()
        # print(rb.GetSelection(), rb.GetStringSelection())  # 打印当前单选按钮的选项
        self.config.saveStep('{0}'.format(rb.GetSelection() + 1))

    def saveIs_Result(self, e):
        rb = e.GetEventObject()
        # print(rb.GetSelection(), rb.GetStringSelection())  # 打印当前单选按钮的选项
        self.config.saveIs_Result('{0}'.format(rb.GetSelection()))

    def saveAdd(self, e):
        rb = e.GetEventObject()
        # print(rb.GetSelection(), rb.GetStringSelection())  # 打印当前单选按钮的选项
        self.config.saveAdd('{0}'.format(rb.GetSelection() + 1))

    def saveSub(self, e):
        rb = e.GetEventObject()
        # print(rb.GetSelection(), rb.GetStringSelection())  # 打印当前单选按钮的选项
        self.config.saveSub('{0}'.format(rb.GetSelection() + 1))

    def saveIs_Bracket(self, e):
        cb = e.GetEventObject()
        if cb.GetValue():
            self.config.saveIs_Bracket("1")
        else:
            self.config.saveIs_Bracket("0")

    def saveJuanzishu(self, e):
        # print(self.text_ctrl_2.GetValue())
        self.config.saveJuanzishu(str(self.text_ctrl_2.GetValue()))

    def saveLieshu(self, e):
        # print(self.text_ctrl_3.GetValue())
        self.config.saveLieshu(str(self.text_ctrl_3.GetValue()))

    def saveJz_title(self, e):
        # print(self.text_ctrl_4.GetValue())
        self.config.saveJz_title(str(self.text_ctrl_4.GetValue()))

    def saveInf_title(self, e):
        # print(self.text_ctrl_5.GetValue())
        self.config.saveInf_title(str(self.text_ctrl_5.GetValue()))

    def saveNumber(self, e):
        # print(self.text_ctrl_16.GetValue())
        self.config.saveNumber(str(self.text_ctrl_16.GetValue()))

    def save_PSM_dir(self, e):
        '''设置口算卷子保存目录
        '''
        dlg = wx.DirDialog(self, message="选择文件夹")
        if dlg.ShowModal() == wx.ID_OK:
            #print(dlg.GetPath())
            self.config.saveDocx(dlg.GetPath())
            wx.MessageBox('设置文件保存目录'+self.config.c.get('config','docx')+os.sep+'docx 成功！', '成功提示',
                          wx.OK | wx.ICON_INFORMATION)

# end of class MyFrame


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.config = AppConfig()
        tmdata = eval(self.config.c.get('config', 'multistep'))
        self.text_ctrl_6 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[0][0]))
        self.text_ctrl_7 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[0][1]))
        self.text_ctrl_8 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[1][0]))
        self.text_ctrl_9 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[1][1]))
        self.text_ctrl_10 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[2][0]))
        self.text_ctrl_11 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[2][1]))
        self.text_ctrl_12 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[3][0]))
        self.text_ctrl_13 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[3][1]))
        self.text_ctrl_14 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[4][0]))
        self.text_ctrl_15 = wx.TextCtrl(
            self, wx.ID_ANY, '{0}'.format(tmdata[4][1]))
        self.button_9 = wx.Button(self, wx.ID_ANY, u"提交修改")
        self.button_9.Bind(wx.EVT_BUTTON, self.onButton_9)
        self.button_10 = wx.Button(self, wx.ID_ANY, u"关闭窗口")
        self.button_10.Bind(wx.EVT_BUTTON, self.onButton_10)
        self.ret = 0  # 算数项设置Dialog返回值

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle(u"运行算项及结果范围数值设置")
        self.text_ctrl_6.SetMinSize((80, 22))
        self.text_ctrl_7.SetMinSize((80, 22))
        self.text_ctrl_8.SetMinSize((80, 22))
        self.text_ctrl_9.SetMinSize((80, 22))
        self.text_ctrl_10.SetMinSize((80, 22))
        self.text_ctrl_11.SetMinSize((80, 22))
        self.text_ctrl_12.SetMinSize((80, 22))
        self.text_ctrl_13.SetMinSize((80, 22))
        self.text_ctrl_14.SetMinSize((80, 22))
        self.text_ctrl_15.SetMinSize((80, 22))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"算数项及结果取值范围"), wx.VERTICAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        label_6 = wx.StaticText(
            self, wx.ID_ANY, u"何为算数项和结果？例如：3+7=10，3和7是算数项，10为结果。")
        sizer_15.Add(label_6, 0, wx.ALL | wx.EXPAND, 5)
        label_7 = wx.StaticText(self, wx.ID_ANY, u"第1个算数项取值范围：")
        sizer_17.Add(label_7, 0, 0, 0)
        sizer_17.Add(self.text_ctrl_6, 0, 0, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_17.Add(label_8, 0, 0, 0)
        sizer_17.Add(self.text_ctrl_7, 0, 0, 0)
        sizer_16.Add(sizer_17, 1, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, u"第2个算数项取值范围：")
        sizer_18.Add(label_9, 0, 0, 0)
        sizer_18.Add(self.text_ctrl_8, 0, 0, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_18.Add(label_10, 0, 0, 0)
        sizer_18.Add(self.text_ctrl_9, 0, 0, 0)
        sizer_16.Add(sizer_18, 1, wx.EXPAND, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, u"第3个算数项取值范围：")
        sizer_19.Add(label_11, 0, 0, 0)
        sizer_19.Add(self.text_ctrl_10, 0, 0, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_19.Add(label_12, 0, 0, 0)
        sizer_19.Add(self.text_ctrl_11, 0, 0, 0)
        sizer_16.Add(sizer_19, 1, wx.EXPAND, 0)
        label_13 = wx.StaticText(self, wx.ID_ANY, u"第4个算数项取值范围：")
        sizer_20.Add(label_13, 0, 0, 0)
        sizer_20.Add(self.text_ctrl_12, 0, 0, 0)
        label_14 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_20.Add(label_14, 0, 0, 0)
        sizer_20.Add(self.text_ctrl_13, 0, 0, 0)
        sizer_16.Add(sizer_20, 1, wx.EXPAND, 0)
        label_15 = wx.StaticText(self, wx.ID_ANY, u"运算结果取值范围：")
        sizer_21.Add(label_15, 0, 0, 0)
        sizer_21.Add(self.text_ctrl_14, 0, 0, 0)
        label_16 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_21.Add(label_16, 0, 0, 0)
        sizer_21.Add(self.text_ctrl_15, 0, 0, 0)
        sizer_16.Add(sizer_21, 1, wx.EXPAND, 0)
        sizer_30.Add(self.button_9, 0, wx.ALIGN_CENTER, 0)
        sizer_30.Add(self.button_10, 0, wx.ALIGN_CENTER, 0)
        sizer_16.Add(sizer_30, 1, wx.ALIGN_CENTER | wx.SHAPED, 0)
        sizer_15.Add(sizer_16, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_15)
        sizer_15.Fit(self)
        self.Layout()
        # end wxGlade

    def onButton_9(self, e):
        self.ret = 1
        self.retdata = [[int(self.text_ctrl_6.GetValue()), int(self.text_ctrl_7.GetValue())],
                        [int(self.text_ctrl_8.GetValue()),
                         int(self.text_ctrl_9.GetValue())],
                        [int(self.text_ctrl_10.GetValue()),
                         int(self.text_ctrl_11.GetValue())],
                        [int(self.text_ctrl_12.GetValue()),
                         int(self.text_ctrl_13.GetValue())],
                        [int(self.text_ctrl_14.GetValue()), int(self.text_ctrl_15.GetValue())]]
        self.EndModal(1)

    def onButton_10(self, e):
        self.EndModal(1)


# end of class MyDialog

class MyDialog1(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog1.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.config = AppConfig()
        self.tmdata = eval(self.config.c.get('config', 'symbols'))
        self.checkbox_2 = wx.CheckBox(self, wx.ID_ANY, u"+(加法)")
        self.checkbox_3 = wx.CheckBox(self, wx.ID_ANY, u"-(减法)")
        self.checkbox_4 = wx.CheckBox(self, wx.ID_ANY, u"×(乘法)")
        self.checkbox_5 = wx.CheckBox(self, wx.ID_ANY, u"÷(除法)")
        self.checkbox_6 = wx.CheckBox(self, wx.ID_ANY, u"+(加法)")
        self.checkbox_7 = wx.CheckBox(self, wx.ID_ANY, u"-(减法)")
        self.checkbox_8 = wx.CheckBox(self, wx.ID_ANY, u"×(乘法)")
        self.checkbox_9 = wx.CheckBox(self, wx.ID_ANY, u"÷(除法)")
        self.checkbox_10 = wx.CheckBox(self, wx.ID_ANY, u"+(加法)")
        self.checkbox_11 = wx.CheckBox(self, wx.ID_ANY, u"-(减法)")
        self.checkbox_12 = wx.CheckBox(self, wx.ID_ANY, u"×(乘法)")
        self.checkbox_13 = wx.CheckBox(self, wx.ID_ANY, u"÷(除法)")
        self.button_9 = wx.Button(self, wx.ID_ANY, u"提交修改")
        self.button_9.Bind(wx.EVT_BUTTON, self.onButton_9)
        self.button_10 = wx.Button(self, wx.ID_ANY, u"关闭窗口")
        self.button_10.Bind(wx.EVT_BUTTON, self.onButton_10)
        self.ret = 0  # 运算符号选择设置Dialog返回值

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog1.__set_properties
        self.SetTitle("运算符号的选择与修改")
        self.checkbox_2.SetValue(int(self.tmdata[0][0]))
        self.checkbox_3.SetValue(int(self.tmdata[0][1]))
        self.checkbox_4.SetValue(int(self.tmdata[0][2]))
        self.checkbox_5.SetValue(int(self.tmdata[0][3]))

        self.checkbox_6.SetValue(int(self.tmdata[1][0]))
        self.checkbox_7.SetValue(int(self.tmdata[1][1]))
        self.checkbox_8.SetValue(int(self.tmdata[1][2]))
        self.checkbox_9.SetValue(int(self.tmdata[1][3]))

        self.checkbox_10.SetValue(int(self.tmdata[2][0]))
        self.checkbox_11.SetValue(int(self.tmdata[2][1]))
        self.checkbox_12.SetValue(int(self.tmdata[2][2]))
        self.checkbox_13.SetValue(int(self.tmdata[2][3]))

        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog1.__do_layout
        sizer_25 = wx.BoxSizer(wx.VERTICAL)
        sizer_26 = wx.BoxSizer(wx.VERTICAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"第3处运算符号选择"), wx.HORIZONTAL)
        sizer_28 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"第2处运算符号选择"), wx.HORIZONTAL)
        sizer_27 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"第1处运算符号选择"), wx.HORIZONTAL)
        label_18 = wx.StaticText(
            self, wx.ID_ANY, u"此处为多步运算题生成运算符号选择，比如4+8-5=，\n你要做的是选择+和-号位置可以使用什么运算符号。")
        sizer_25.Add(label_18, 0, wx.ALL | wx.EXPAND, 5)
        sizer_27.Add(self.checkbox_2, 0, 0, 0)
        sizer_27.Add(self.checkbox_3, 0, 0, 0)
        sizer_27.Add(self.checkbox_4, 0, 0, 0)
        sizer_27.Add(self.checkbox_5, 0, 0, 0)
        sizer_26.Add(sizer_27, 1, wx.EXPAND, 0)
        sizer_28.Add(self.checkbox_6, 0, 0, 0)
        sizer_28.Add(self.checkbox_7, 0, 0, 0)
        sizer_28.Add(self.checkbox_8, 0, 0, 0)
        sizer_28.Add(self.checkbox_9, 0, 0, 0)
        sizer_26.Add(sizer_28, 1, wx.EXPAND, 0)
        sizer_29.Add(self.checkbox_10, 0, 0, 0)
        sizer_29.Add(self.checkbox_11, 0, 0, 0)
        sizer_29.Add(self.checkbox_12, 0, 0, 0)
        sizer_29.Add(self.checkbox_13, 0, 0, 0)
        sizer_26.Add(sizer_29, 1, wx.EXPAND, 0)
        sizer_30.Add(self.button_9, 0, wx.ALIGN_CENTER, 0)
        sizer_30.Add(self.button_10, 0, wx.ALIGN_CENTER, 0)
        sizer_26.Add(sizer_30, 1, wx.ALIGN_CENTER, 0)
        sizer_25.Add(sizer_26, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_25)
        sizer_25.Fit(self)
        self.Layout()
        # end wxGlade

    def getsymbols(self, a, b, c, d):
        '''根据值判断添加需要的算数符号'''
        tmplist = []
        if a.GetValue():
            tmplist.append(1)
        else:
            tmplist.append(0)
        if b.GetValue():
            tmplist.append(2)
        else:
            tmplist.append(0)
        if c.GetValue():
            tmplist.append(3)
        else:
            tmplist.append(0)
        if d.GetValue():
            tmplist.append(4)
        else:
            tmplist.append(0)

        return tmplist

    def onButton_9(self, e):
        self.ret = 1
        self.retdata = [self.getsymbols(self.checkbox_2, self.checkbox_3, self.checkbox_4, self.checkbox_5),
                        self.getsymbols(
                            self.checkbox_6, self.checkbox_7, self.checkbox_8, self.checkbox_9),
                        self.getsymbols(self.checkbox_10, self.checkbox_11, self.checkbox_12,
                                        self.checkbox_13)]  # 默认运算符号值
        self.EndModal(1)

    def onButton_10(self, e):
        self.EndModal(1)


# end of class MyDialog1

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
