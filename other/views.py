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
    users = itchat.search_friends(name=name)
    print(users)
    data_fin = {}
    if users:
        user_id = users[0]['UserName']
        content = query_weather(city)
        date = content.get("date")
        weather = content.get("weather")
        temperature = content.get("temperature")
        wind = content.get("wind")
        llist = []
        for d, w, t, wind, num in zip(date, weather, temperature, wind, [1, 2, 3, 4, 5]):
            to = ''
            if num == 1:
                to = "今天"
            if num == 2:
                to = "明天"
            if num == 3:
                to = "后天"
            if num == 4:
                to = "大后天"
            if num == 5:
                to = "大大后天"
            llist.append("{}：{}，天气：{}，温度：{}，风度：{}".format(to, d, w, t, wind))
        # content = json.dumps(content, ensure_ascii=False)
        msgs = "最近五天{}天气如下：".format(city) + "\n\n" + "\n\n".join(llist)
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
