import requests
from send_msg.models import CITY
from django.conf import settings


def city_code(city):
    city = CITY.objects.filter(city_name__contains=city)
    if city.exists():
        return True, city.first().city_code
    else:
        return False, 0


def city_weather(code):
    resp = requests.get(url=settings.WEATHER_UEL.format(city_code=code))
    return resp.json()


def query_weather(city_name):
    status, code = city_code(city_name)
    if not status:
        return False, "城市不存在"
    return city_weather(code)


if __name__ == '__main__':
    pass
