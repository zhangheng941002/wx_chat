import requests
from send_msg.models import CITY
from django.conf import settings

GD_URL = settings.GD_URL
GD_KEY = settings.GD_KEY


def query_weather(city, province=None, _type=0):
    """
    查询天气封装接口
    :param city: 城市或区名
    :param province: 省份或直辖市名称
    :param _type: 查看类型：默认查询天气预报，0/1:查询天气预报/实时天气
    :return:
    """

    if _type:
        extensions = "base"
    else:
        extensions = "all"
    if province:
        _citys = CITY.objects.filter(city_name__contains=province)
        if not _citys.exists():
            return False, None
        city_code = _citys.first().citycode
        _city = CITY.objects.filter(citycode=city_code)
    else:
        _city = CITY.objects.all()
    _city_info = _city.filter(city_name__contains=city)
    if not _city_info.exists():
        return False, None
    code = _city_info.first().adcode
    url = f"{GD_URL}/weather/weatherInfo?key={GD_KEY}&city={code}&extensions={extensions}"
    resp = requests.get(url)
    _resp = resp.json()
    _resp["status"] = int(_resp.get("status"))

    return True, _resp


if __name__ == '__main__':
    pass
