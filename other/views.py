from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

import itchat
import json
import random

from utils.query_weather_utils import query_weather
from helper.log_help import *


@api_view(["GET"])
def send_to_smy(request):
    """
    给好友发送天气
    :param request:
                city:城市
                name:好友的备注名称
    :return:
    """

    full_path = request.get_full_path()
    data = request.GET
    name = data.get("name", settings.LOVE)
    city = data.get("city", settings.LOVE_WHERE)
    day = data.get("city", settings.WEATHER_DAYS)
    users = itchat.search_friends(name=name)
    print('===============================')
    print(users)
    print('===============================')

    data_fin = {}
    if users:
        user_id = users[0]['UserName']
        content = query_weather(city)
        cityInfo = content.get("cityInfo")
        data = content.get("data")
        shidu = data.get("shidu")
        pm25 = data.get("pm25")
        pm10 = data.get("pm10")
        quality = data.get("quality")
        wendu = data.get("wendu")
        ganmao = data.get("ganmao")
        forecast = data.get("forecast")

        llist = []
        map_key = {
            "ymd": "",  # 日期
            "week": "",  # 星期
            "high": "最高温度：",
            "low": "最低温度：",
            # "sunrise": "日出：",
            # "sunset": "日落：",
            "aqi": "空气指数：",
            "fx": "风向：",
            "fl": "风力：",
            "type": "天气：",
            "notice": "温馨提示："
        }
        for each in forecast:
            """
                "date": "26",
                "high": "高温 28℃",
                "low": "低温 20℃",
                "ymd": "2020-06-26",
                "week": "星期五",
                "sunrise": "04:47",
                "sunset": "19:49",
                "aqi": 49,
                "fx": "东南风",
                "fl": "2级",
                "type": "多云",
                "notice": "阴晴之间，谨防紫外线侵扰"
            """
            _data = {}
            _msg = ""
            for k, v in map_key.items():
                _msg += str(v)
                if k in ["high", 'low']:
                    _msg += str(each[k][3:])
                else:
                    _msg += str(each[k])
                _msg += "\n"
            llist.append(_msg)

        msgs = "{}最近{}天天气如下：".format(cityInfo.get("parent")+cityInfo.get("city"), day) + "\n\n" + "\n\n".join(llist[:day])
        res = itchat.send(msgs, toUserName=user_id)
        res = res.get("BaseResponse").get("Ret")
        if res == 0:
            msg = "发送成功"
        elif res == -1:
            msg = "你查询的群组不存在！发送失败"
        else:
            msg = "发送失败"
        data_fin = {"status": 1, "msg": "{}，{}".format(msg, content)}
    logg(full_path, data_fin)
    return Response(data_fin)


@api_view(["GET"])
def send_to_smy_qh(request):
    """

    """

    full_path = request.get_full_path()
    data = request.GET
    name = data.get("name", settings.LOVE)
    users = itchat.search_friends(name=name)
    print(users)
    data_fin = {}
    if users:
        user_id = users[0]['UserName']

        res = itchat.send("今日份情话：{}".format(settings.LOVE_MSG[random.randint(0, 60)]), toUserName=user_id)
        print(res)
        res = res.get("BaseResponse").get("Ret")
        if res == 0:
            msg = "发送成功"
        elif res == -1:
            msg = "你查询的群组不存在！发送失败"
        else:
            msg = "发送失败"
        data_fin = {"status": 1, "msg": "{}，{}".format(msg, settings.LOVE_MSG[random.randint(0, 60)])}
    logg(full_path, data_fin)
    return Response(data_fin)
