'''
Author: J.sky bosichong@qq.com
Date: 2022-11-15 08:18:31
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-12-01 23:56:49
FilePath: /PrimarySchoolMath/webbackend/main.py
开心Python Flask Django 学习交流q群：217840699
Author  : J.sky
Mail    : bosichong@qq.com
特别感谢以下二位大佬的鼎力支持！
Author  : rcddup
Mail    : 410093793@qq.com
Author  : andywu1998
Mail    : 1078539713@qq.com
'''

import json
import sys
import os
from fastapi.staticfiles import StaticFiles
from utils import make_docx_dirs
from Psmrcddup import Generator
from PrintPreview import PrintPreview
from APPconfig import AppConfig
from pydantic import BaseModel
import uvicorn as uvicorn
from starlette.responses import Response
from fastapi.responses import HTMLResponse  # 导出html
from fastapi.middleware.cors import CORSMiddleware  # 解决跨域
from fastapi import FastAPI, HTTPException
import random


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

__version__ = "1.2.1"

description = """
PrimarySchoolMath一套自动生成小学生口算题的小应用. 🚀
"""

app = FastAPI(
    title="PrimarySchoolMath",
    description=description,
    version=__version__,
    terms_of_service="#",
    license_info={
        "name": "Apache 2.0",
        "url":  "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# 配置允许域名
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8000"
    "http://localhost:8000",

]
# 配置允许域名列表、允许方法、请求头、cookie等
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/dist", StaticFiles(directory=os.path.join(BASE_DIR,
          'webbackend/dist')), name="dist")
app.mount("/assets", StaticFiles(directory=os.path.join(BASE_DIR,
          'webbackend/dist/assets')), name="assets")

# APP配置文件对象
appConfig = AppConfig()


@app.get("/")
def main():
    html_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'dist', 'index.html')
    html_content = ''
    with open(html_path, encoding="utf-8") as f:
        html_content = f.read()

    return HTMLResponse(content=html_content, status_code=200)


@app.get("/test")
def test(data: str):
    return data


@app.get("/api_getconfigjson")
def getConfigJson():
    """
    打开程序首页后加载程序的默认配置
    """
    # print(appConfig.loadINI())
    rs = {'config': appConfig.loadINI(), }
    return rs


class Psm_A(BaseModel):
    '''
    验证口算题的模型
    '''
    data: dict


@app.post('/api_createpsm')
def createpsm(data: Psm_A):
    """创建一组口算题的配置,接收前端送来的一组口算题配置，判断配置是否合法。"""
    jsondata = data.data
    # print(jsondata)
    rs = {"info": isZeroA(jsondata["step"],
                          jsondata["multistep"], jsondata["symbols"], jsondata["number"], jsondata["div"]["remainder"],
                          jsondata["is_result"])}
    return rs


class Psm_Data(BaseModel):
    data: str


@app.post('/api/psm')
def generate_psm(data: Psm_Data):
    '''
    接受前端发来的口算题配置生成口算题并保存到文件
    '''
    jsonData = json.loads(data.data)

    # 验证
    if len(jsonData[0]) == 0:
        raise HTTPException(status_code=400, detail='还没有添加口算题到列表中哈！')

    # 生成试卷
    produce_PSM(jsonData)

    # 获取试卷地址以供下载
    baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docxPath = os.path.join(baseDir, 'webbackend/dist/docx')  # 前端docx文件夹
    docxList = getpathfile(docxPath)
    return docxList


@app.get('/getpsmlist')
def getpsmlist():
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docxpath = os.path.join(basedir, 'webbackend/dist/docx')  # 前端docx文件夹
    docxs = getpathfile(docxpath)
    # print(docxs)
    return docxs


def getRstr(isok):
    """
    根据判断返回口算题是否生成的提示文字
    :param isok bool
    :return bool
    """

    if isok:
        rs = {"info": "口算题生成完毕！"}
    else:
        rs = {"info": "程序运行失败！是不是还没有添加口算题就点了生成按钮？"}
    return rs


def isZeroA(step, multistep, symbols, number, remainder, is_result):
    '''
    运算中除数<=0的判断,及除法结果有余数是不能是用求算数项
    '''
    # TODO
    # 请添加运算符号为空的错误提示,当运算符号没有选择的时候程序运行会出错
    # 还有算数项最小数值大于最大数值的时候程序会出错，也要判断以下。一步运算的时候开启括号会添加括号
    #
    # print(multistep, multistep[1][0])
    if (4 in symbols[0] and multistep[1][1] <= 0) or (
            4 in symbols[1] and multistep[2][1] <= 0) or (
            4 in symbols[2] and multistep[3][1] <= 0):
        return 0
    # print(remainder,is_result)
    if (remainder != 2 and is_result == 1) or (remainder != 2 and step > 1):
        return 0  # 求算数项是不能有余数，多步的运算的时候不能有余数

    str_number = str(number)
    if step == 1:
        # todo 后续修改为反馈详细的添加信息，例如 X步计算加、减口算题XX道
        return "一步计算口算题" + str_number + "道|||"
    elif step == 2:
        return "两步计算口算题" + str_number + "道|||"
    elif step == 3:
        return "三步计算口算题" + str_number + "道|||"


def produce_PSM(json_data):
    '''发布口算题保存.docx文件'''
    psm_list = []  # 口算题列表
    psm_title = []  # 标题列表

    # 循环生成每套题
    for i in range(json_data[1]["juanzishu"]):
        paper = getPsmList(json_data)  # 生成一页口算题

        # 处理自定义题目,如果有自定义题目也加入到试卷中
        if (json_data[2]):  # 约定数组的第三项是自定义题目配置
            customFormulaOptions = json_data[2]
            for option in customFormulaOptions:
                for c in option["customFormulaList"]:
                    paper.append(c["formula"])

        random.shuffle(paper)  # 随机打乱
        psm_list.append(paper)  # 添加到list 准备后期打印
        # 为生成的文件起名r
        # psm_title.clear()

    for i in range(json_data[1]["juanzishu"]):
        psm_title.append(json_data[1]["jz_title"])
    # print(self.psm_title)
    subtit = json_data[1]["inf_title"]

    # print(psm_list)

    pp = PrintPreview(psm_list, psm_title, subtit,
                      col=json_data[1]["lieshu"], solution=json_data[1]['solution'], fileNameGeneratedRule=json_data[1]["fileNameGeneratedRule"])
    pp.delpath()  # 删除之前的口算题
    pp.produce()  # 生成docx
    pp.filetovuepublicdocx()  # 复制新的口算题到前端目录
    pp.docxtozip()  # 打包zip到vue 目录下变提供下载
    psm_list.clear()  # 清空打印列表。
    # print(type(json_data))
    # appConfig.saveAll(json_data)  # 保存所有配置项
    # self.movdocx()


def getPsmList(json_data):
    '''
    根据配置文件生成一套口算题的所有题
    :param json_data 口算题的所有配置
    :return list 最终的口算题页
    '''
    templist = []
    for j in json_data[0]:
        # j = json.loads(j)
        g = Generator(addattrs=j["add"], subattrs=j["sub"], multattrs=j["mult"], divattrs=j["div"],
                      symbols=j["symbols"], multistep=j[
            "multistep"], number=j["number"], step=j["step"],
            is_result=j["is_result"], is_bracket=j["is_bracket"], )
        templist = templist + g.generate_data()
    return templist


def q_PSM(json_data):
    '''
    命令行快速生成口算题
    :json_data 口算题配置文件
    '''
    psm_list = []  # 口算题列表
    psm_title = []  # 标题列表
    for i in range(json_data[1]["juanzishu"]):
        templist = getPsmList(json_data)  # 生成一页口算题
        random.shuffle(templist)  # 随机打乱
        psm_list.append(templist)  # 添加到list 准备后期打印
        # 为生成的文件起名r
        # psm_title.clear()

    for i in range(json_data[1]["juanzishu"]):
        psm_title.append(json_data[1]["jz_title"])

    subtit = json_data[1]["inf_title"]  # 小标题
    pp = PrintPreview(psm_list, psm_title,
                      subtit, col=json_data[1]["lieshu"], )

    pp.produce()  # 生成docx
    psm_list.clear()  # 清空打印列表。
    return 1


def getpathfile(path):
    '''返回当前目录下的文件名称'''
    path_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".docx"):
                path_list.append(f)
    return path_list


if __name__ == '__main__':
    print('少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了')
    make_docx_dirs()
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, )
