import requests
from send_msg.models import CITY
from django.conf import settings

GD_URL = settings.GD_URL
GD_KEY = settings.GD_KEY


def query_weather(city, _type=0):
    if _type:
        extensions = "base"
    else:
        extensions = "all"

    _city_info = CITY.objects.filter(city_name__contains=city)
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
