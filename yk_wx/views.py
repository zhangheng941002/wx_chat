from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_all_url(request):
    print (request.get_full_path, '------------')
    ip = request.META.get("REMOTE_ADDR")
    HTTP_HOST = request.META.get("HTTP_HOST")
    HTTP_TYPE = request.META.get("wsgi.url_scheme")
    HEADER = HTTP_TYPE + "://" + HTTP_HOST
    data = {
        "登录：": HEADER + "/send_msg/login",
        "二维码下载：": HEADER + "/send_msg/qr_code_load",
        "退出登录：": HEADER + "/send_msg/logout",
        "验证是否登录：": HEADER + "/send_msg/check",
        # "获取群组：": HEADER + "/send_msg/get_group",
        # "创建群组：": HEADER + "/send_msg/create_group",
        "获取好友：": HEADER + "/send_msg/get_friend",
        # "给群组发消息：": HEADER + "/send_msg/send_to_group",
        "给好友发消息：": HEADER + "/send_msg/send_to_friend",
        "获取所有URL：": HEADER + "/send_msg/get_all_url",
        "查询天气：": HEADER + "/love/get_weather",


    }
    return Response(data)

