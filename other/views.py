from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

import itchat
import random

from utils.query_weather_utils import query_weather
from utils.log_help import *
from utils.gd_weather_data.notice_map import *


@api_view(["GET"])
def send_to_user_weather(request):
    """
    给好友发送天气
    :param request:
                city:城市
                province: 省份或直辖市名称
                name:好友的备注名称
                days:查看几天的天气，该接口可查询出四天的信息，默认3天，后三天的
                opt_type: 查看类型：默认后三天天气，opt_type=1,
                                                    opt_type=2:查看当天天气
    :return:
    """

    full_path = request.get_full_path()
    data = request.GET
    name = data.get("name", settings.LOVE)
    city = data.get("city", settings.LOVE_WHERE)
    province = data.get("province", None)
    opt_type = data.get("opt_type", 1)
    day = data.get("days", settings.WEATHER_DAYS)
    users = itchat.search_friends(name=name)
    # users = 1
    print('===============================')
    print(users)
    print('===============================')

    data_fin = {}
    if users:
        user_id = users[0]['UserName']
        status, content = query_weather(city, province)
        if not status:
            return Response({"status": 0, "msg": "没有查到城市"})

        forecast = content.get("forecasts")[0]
        city_info = "{} {}".format(forecast.get("province"), forecast.get("city"))
        casts = forecast.get("casts")
        llist = []
        map_key = {
            "date": "",  # 日期
            "week": "",  # 星期
            "daytemp": "最高温度：",
            "nighttemp": "最低温度：",
            "daywind": "风向：",
            "daypower": "风力：",
            "dayweather": "天气：",
        }
        if opt_type == 1:
            q_range = casts[1:]
        elif opt_type == 2:
            q_range = casts[:1]
        else:
            q_range = casts[1:]
        for each in q_range:
            """
                "date": "2020-07-22", # 日期
                "week": "3",  # 星期几
                "dayweather": "大雨",  # 白天天气现象
                "nightweather": "暴雨",  # 晚上天气现象
                "daytemp": "27",  # 白天温度
                "nighttemp": "22",  # 晚上温度
                "daywind": "南",  # 白天风向
                "nightwind": "南",  # 晚上风向
                "daypower": "4",  # 白天风力
                "nightpower": "4"  # 晚上风力
            """
            _data = {}
            _msg = ""
            for k, v in map_key.items():

                _msg += str(v)
                if k in ["high", 'low']:
                    _msg += str(each[k][3:])
                elif k == "week":
                    _msg += settings.WEEK_MAP[each[k]]
                else:
                    _msg += str(each[k])
                _msg += "\n"
                if k == "dayweather":
                    _msg += "温馨提醒："
                    _notice = "I love you"
                    for _k, _v in WEATHER_DATA.items():
                        if str(each[k]) in _v:
                            _notice = NOTICE_MAP[_k][random.randint(0, 2)]
                            break
                    _msg += _notice

            llist.append(_msg)

        msgs = "{}最近{}天天气如下：".format(city_info, day) + "\n\n" + "\n\n".join(llist[:day])
        res = itchat.send(msgs, toUserName=user_id)
        print("----------- send msg response:-------", res)
        res = res.get("BaseResponse").get("Ret")
        if res == 0:
            msg = "发送成功"
        elif res == -1:
            msg = "你查询的群组不存在！发送失败"
        else:
            msg = "发送失败"

        data_fin = {"status": 1, "msg": "{}，{}".format(msg, content)}
    # logg(full_path, data_fin)
    return Response(data_fin)


@api_view(["GET"])
def send_to_qh(request):
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
    # logg(full_path, data_fin)
    return Response(data_fin)
