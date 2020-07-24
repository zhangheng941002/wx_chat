from django.conf.urls import url
from .views import *
from .views_render import *


urlpatterns = [
    url(r'send_weather$', send_to_user_weather),
    url(r'send_to_qh$', send_to_qh),
    url(r'gd_query_weather$', gd_query_weather),
    url(r'query_ip_area$', query_ip_area),
    url(r'query_phone$', query_phone),


]
