from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_all_url(request):
    ip = request.META.get("REMOTE_ADDR")
    HTTP_HOST = request.META.get("HTTP_HOST")
    HTTP_TYPE = request.META.get("wsgi.url_scheme")
    HEADER = HTTP_TYPE + "://" + HTTP_HOST
    data = {
        "wx_api": {
            "登录：": HEADER + "/send_msg/login",

            "二维码下载：": HEADER + "/send_msg/qr_code_load",

            "退出登录：": HEADER + "/send_msg/logout",

            "验证是否登录：": HEADER + "/send_msg/check",

            "获取好友：": HEADER + "/send_msg/get_friend",

            "将有备注的好友加入自动回复：": HEADER + "/send_msg/auto_add_chat",

            "取消好友自动回复：": HEADER + "/send_msg/auto_del_chat",

            "给好友发消息：": HEADER + "/send_msg/send_to_friend",

            "给好友发送天气提醒：": HEADER + "/other/send_weather",

            "给指定好友发送情话：": HEADER + "/other/send_to_qh",

            "获取群组：": HEADER + "/send_msg/get_group",

            "创建群组：": HEADER + "/send_msg/create_group",

            "添加好友进某一群组：": HEADER + "/send_msg/add_user_to_group",

            "给群组发消息：": HEADER + "/send_msg/send_to_group",
        },
        "other_api": {
            "查询天气：": HEADER + "/other/gd_query_weather",

            "IP定位：": HEADER + "/other/query_ip_area",

            "手机号归属地查询：": HEADER + "/other/query_phone",

            "获取所有URL：": HEADER + "/get_all_url", }

    }
    return Response(data)
