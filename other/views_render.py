# -*- coding:utf-8 -*-
# author:zh
# datetime:2019/12/11 上午9:10

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils.query_weather_utils import query_weather


@api_view(["GET"])
def get_weather(request):
    """
    查询某个城市最近五天的天气
    :param request:
                    city:查询的城市

    :return:
    """
    data = request.GET
    city = data.get("city", "北京")
    code = data.get("code")

    content = query_weather(city)
    del content["message"]
    return Response(content)