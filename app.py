# -*- coding=utf-8 -*-
'''

开心Python flask Django 学习交流q群：217840699


Author  : J.sky
Mail    : bosichong@qq.com


特别感谢一下二位大佬的鼎力支持！

Author  : rcddup
Mail    : 410093793@qq.com

Author  : andywu1998
Mail    : 1078539713@qq.com


'''

from flask import Flask, render_template, jsonify, request

import json

from .APPconfig import AppConfig


app = Flask('web')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.secret_key = 'secret string'


# APP配置文件 对象
appConfig = AppConfig()  # 程序配置文件对象


@app.route('/')
def index():
    return render_template("index.html",)


@app.route('/api_getConfigJson')
def getConfigJson():
    '''
    打开程序首页后加载程序的默认配置
    '''
    # print(appConfig.loadINI())
    rs = {'config': appConfig.loadINI(), }
    return jsonify(rs)


@app.route('/api_createPSM', methods=['POST'])
def createPSM():
    '''
    创建一组口算题的配置,接收前端送来的一组口算题配置，判断配置是否合法。
    '''
    jsondata = request.get_json()
    # print(jsondata)
    rs = {"info": isZeroA(jsondata["step"], jsondata["signum"],
                          jsondata["multistep"], jsondata["symbols"], jsondata["number"])}
    return jsonify(rs)


@app.route('/api_producePSM', methods=['POST'])
def producePSM():
    jsondata = request.get_json()
    print(jsondata)
    rs = {"info": "口算题生成完毕！"}
    return jsonify(rs)

#############################


def isZeroA(step, signum, multistep, symbols, number):
    '''
    运算中除数<=0的判断
    '''

    if step == 1 and signum == 4:
        if multistep[1][0] <= 0:
            return 0

    # 多步运算时除法余数为零判断
    if step > 1:
        if (4 in symbols[0] and multistep[1][0] <= 0) or (
                4 in symbols[1] and multistep[2][0] <= 0) or (
                4 in symbols[2] and multistep[3][0] <= 0):
            return 0

    str_number = str(number)
    if step == 1:
        if signum == 1:
            return "加法口算题" + str_number + "道|||"
        elif signum == 2:
            return "减法口算题" + str_number + "道|||"
        elif signum == 3:
            return "乘法口算题" + str_number + "道|||"
        elif signum == 4:
            return "除法口算题" + str_number + "道|||"
        else:
            raise Exception("没有这个题型哦")
    elif step == 2:
        return "两步计算口算题" + str_number + "道|||"

    elif step == 3:
        return "三步计算口算题" + str_number + "道|||"
