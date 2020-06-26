from django.conf.urls import url
from .views import *
from .views_render import *


urlpatterns = [
    url(r'send_weather$', send_to_smy),
    url(r'send_love_msg$', send_to_smy_qh),
    url(r'get_weather$', get_weather),


]
