# -*- coding:utf-8 -*-
# author:zh
# datetime:2019/12/11 上午9:10

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from utils.query_weather_utils import query_weather
from utils.util import OPTPhone
from django.conf import settings

GD_URL = settings.GD_URL
GD_KEY = settings.GD_KEY


@api_view(["GET"])
def query_ip_area(request):
    """
    查询IP所属区域，只支持国内的
    IP
    province:省份名称，若为直辖市则显示直辖市名称；如果在局域网 IP网段内，则返回“局域网”；非法IP以及国外IP则返回空
    """
    '''获取请求者的IP信息'''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if x_forwarded_for:
        _ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
    else:
        _ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    data = request.GET
    ip = data.get("ip", _ip)
    url = f"{GD_URL}/ip?key={GD_KEY}&ip={ip}"
    resp = requests.get(url)
    _resp = resp.json()
    _resp["status"] = int(_resp.get("status"))
    return Response(_resp)


@api_view(["GET"])
def gd_query_weather(request):
    """
    查询天气
    城市名称
    查询类型，默认查询天气预报，_type：1/0 -->实时/天气预报（4天）

    """
    data = request.GET
    _type = int(data.get("_type", 0))
    city = data.get("city", "北京市")
    status, _resp = query_weather(city, _type)
    if not status:
        return Response({"status": 0, "msg": "没有要查的城市"})
    return Response(_resp)


@api_view(["GET"])
def query_phone(request):
    """
    手机号归属地查询
    支持号段: 13*,15*,18*,14[5,7],17[0,6,7,8]
    :return:
            {
                "phone": "15701350657",
                "province": "北京",
                "city": "北京",
                "zip_code": "100000",
                "area_code": "010",
                "phone_type": "移动"
            }
    """
    data = request.query_params
    phone = data.get("phone", None)
    if phone:
        zh = OPTPhone()
        resp = zh.find_phone(phone)
    else:
        resp = {}
    return Response(resp)