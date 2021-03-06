from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'login', login),
    url(r'logout', logout),
    url(r'check', check_IF_login),
    url(r'qr_code_load', big_file_download),

    url(r'get_friend', get_friend),
    url(r'send_to_friend', send_to_friend),
    url(r'auto_add_chat', auto_add_chat),
    url(r'auto_del_chat', auto_del_chat),

    url(r'get_group', get_group),
    url(r'create_group', create_group),
    url(r'add_user_to_group', add_user_to_group),
    url(r'send_to_group', send_to_group),


    url(r'insert_data', insert_data),

]
