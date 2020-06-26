# -*- coding:utf-8 -*-
# author:zh
# datetime:2019/12/11 上午9:10

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils.query_weather_utils import query_weather
from utils.query_ip_utils import query_ip_attribution, query_your_own_ip


@api_view(["GET"])
def get_weather(request):
    """
    查询某个城市最近五天的天气
    :param request:
                    city:查询的城市
                    code:返回的数据样式，1：json
    :return:
    """
    data = request.GET
    city = data.get("city", "北京")
    code = data.get("code")

    content = query_weather(city)
    if code == "1":
        return Response(content)
    date = content.get("date")
    weather = content.get("weather")
    temperature = content.get("temperature")
    wind = content.get("wind")
    llist = ["{} 最近五天的天气情况如下：".format(city)]
    for d, w, t, wind, num in zip(date, weather, temperature, wind, [1, 2, 3, 4, 5]):
        llist.append("{}，  天气：{}，  温度：{}，  风度：{}".format(d, w, t, wind))
    return render(request, 'weather.html', {'title': "查询天气", "content": llist})


@api_view(["GET"])
def get_ip_info(request):
    """
    查询IP信息，默认查询使用电脑
    :param request:
                ip:要查询的IP，不传默认本机IP
                code:返回的数据样式， 1：json
    :return:
    """
    data = request.GET
    code = data.get("code")
    ip = data.get("ip")
    if not ip:
        # ip = query_your_own_ip()
        return render(request, 'ip.html', {'title': "IP的信息", "content": {"status": 0}})

    ips = query_ip_attribution(ip)
    if code == "1":
        return Response(ips)

    return render(request, 'ip.html', {'title': "IP的信息", "content": ips})


@api_view(["GET"])
def get_yourself_ip(request):
    """
    查询IP信息，默认查询使用电脑
    :param request:
                ip:要查询的IP，不传默认本机IP
                code:返回的数据样式， 1：json
    :return:
    """
    data = request.GET
    code = data.get("code")
    ip = query_your_own_ip()

    if code == 1:
        return Response(ip)

    return render(request, 'ip.html', {'title': "查询出网IP", "content": ip})
