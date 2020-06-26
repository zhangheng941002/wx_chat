from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import itchat
from django.http import StreamingHttpResponse

from yk_wx.setting_itchat import path_file
from .serializers import *

from yk_wx.city_code import city
from .models import CITY
from django.http import JsonResponse
from helper.log_help import *

now_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)


@api_view(["GET"])
def check_IF_login(request):
    print(request.get_full_path())
    ourself_info = itchat.get_friends()
    if ourself_info:
        return Response({"status": 1, "msg": "微信已在线", "url": "https://www.baidu.com"})
    else:

        return Response({"status": 1, "msg": "微信已不在线，请重新登录", "url": "https://www.baidu.com"})


# 退出微信登录
@api_view(["GET"])
def logout(request):
    res = itchat.logout()
    print('-----------', res)
    # print(res.get("BaseResponse"))
    status = res.get("BaseResponse").get("status")
    if status == 1:
        # if os.path.exists(path_file) and itchat_in:
        #     os.remove(path_file)
        #     os.remove(itchat_in)
        return Response({"status": status})
    else:
        return Response({"status": 0})


@api_view(["GET"])
def login(request):
    if settings.AUTO_CHAT:
        def get_response(info):
            from qqai import TextChat

            siri = TextChat("2125667918", "YBCQnC3q4PLQAGNN")

            # 单句对话
            answer = siri.ask(info)
            print('------ 自动回复 -------', answer)
            return answer

        @itchat.msg_register(itchat.content.TEXT)
        def text_reply(msg):
            try:
                user = msg['User']
                print('---- 发送人 NickName：{}，备注：{} -------- 发送消息：{}'.format(user['NickName'], user['RemarkName'],
                                                                           msg['Text']))
            except Exception as e:
                print(' !!!!!!!!!!!!! 发送错误-----', str(e))
            return "【自动回复→ZH的机器人】" + "\n" + get_response(msg["Text"])
            # return "【自动回复】" + "\n" + "我是机器人，不会聊天，请找主人说事"

        res = itchat.auto_login(hotReload=True)
        itchat.run()
    res = itchat.auto_login(hotReload=True, enableCmdQR=True)
    status = 1
    print(res)
    return Response({"status": status})


# 查询群组
@api_view(["GET"])
def get_group(request):
    """
    查询群组
    :param request: page_size,page_no,group_name
    demo:  /send_msg/get_group?group_name=测试1
    """

    full_path = request.get_full_path()
    group_name = request.GET.get("group_name", "")
    groups = itchat.search_chatrooms(name=group_name)
    print('------------------- groups ----------------------------')
    print(groups)
    print('------------------- groups ----------------------------')
    data = {}

    if groups:
        group = groups[0]
        data['UserName'] = group.get("UserName")
        data['NickName'] = group.get("NickName")
        data['MemberCount'] = group.get("MemberCount")
        data['MemberList'] = group.get("MemberList")

    logg(full_path, request.GET, {})
    return Response({"status": 1, "results": data})


# 创建群组
@api_view(["POST"])
def create_group(request):
    """
    先调用iechat查询接口，找出ID，插入数据库
    :param request: group_name,operator
    demo: {
            "group_name":"测试",
            "operator": "admin"
            }
    """

    full_path = request.get_full_path()
    path = request.path
    data = request.data
    group_name = data.get("group_name")
    operator = data.get("operator")
    print(group_name)
    group_filter = WXGROUP.objects.filter(group_name=group_name)
    if group_filter:
        return Response({"status": 0, "msg": "你要创建的群组已存在"})

    status = 1
    groups = itchat.search_chatrooms(name=group_name)
    if groups:
        # group_id = groups[0]['UserName']
        list11 = []
        for each in groups:
            if group_name == each['NickName']:
                list11.append(group_name)
        if group_name in list11:
            WXGROUP.objects.create(operator=operator, group_name=group_name, operate_date=now_time)
            msg = "创建成功"
        else:
            msg = "创建失败，没有找到你所要创建的群组"
            status = 0
    else:
        msg = "创建失败，没有找到你所要创建的群组"
        status = 0
    data_fin = {"status": status, "msg": msg}
    logg(full_path, data, data_fin)
    return Response(data_fin)


# 给群组发消息
@api_view(["POST"])
def send_to_group(request):
    """
    通过 group_name 实时查找group_id 给群组发消息
    :param request: group_name，content
    demo: {
            "group_name":"测试1",
            "content":"同名群组测试"
            }
    备注：该群组你需要先保存到通讯录才可以发送！

    """

    full_path = request.get_full_path()
    data = request.data
    group_name = data.get("group_name")
    content = data.get("content")  # + str(now_time)

    groups = itchat.search_chatrooms(name=group_name)
    warning = ""
    status = 1
    error_num = 0
    right_num = 0
    if len(groups) > 1:
        warning = "您所发送的群组，经查找有{}个同名群组!".format(len(groups))
    for each in groups:
        group_id = each['UserName']
        res = itchat.send(content, toUserName=group_id)

        print(res)
        res = res.get("BaseResponse").get("Ret")
        if res == 0:
            right_num += 1
        elif res == -1:
            status = 0
            error_num += 1
        else:
            status = 0
            error_num += 1
    msg = "发送成功：{}个，发送失败：{}".format(right_num, error_num)
    if len(groups) > 1:
        msg = warning + msg
    else:
        if status == 1:
            msg = "发送成功"
        else:
            msg = "发送失败"

    if len(groups) == 0:
        msg = "没有找到群组，请核对群组名是否有效！"
        status = 0
    data_fin = {"status": status, "msg": msg, }
    logg(full_path, data, data_fin)
    return Response(data_fin)


# 查询好友
@api_view(["GET"])
def get_friend(request):
    """
    查询好友
    :param request: friend_name
    demo: /send_msg/get_friend?friend_name=舒良松
    """

    full_path = request.get_full_path()
    friend_name = request.GET.get("friend_name", "")
    list_fin = []

    if friend_name:
        users = itchat.search_friends(name=friend_name)
        data = {}
        if users:
            user_id = users[0]['UserName']
            user_orign_name = users[0]['NickName']
            user_note = users[0]['RemarkName']
            data["user_id"] = user_id
            data["user_orign_name"] = user_orign_name
            data["user_note"] = user_note
            list_fin.append(data)
            msg = "查询成功"
        else:

            msg = "未查询到搜索好友"
    else:

        # 获取通讯录信息，所有好友信息

        friend_list = itchat.get_friends()[1:]  # 第一个是自己的信息，去掉
        for each_friend in friend_list:
            data_ea = {}
            user_id = each_friend.UserName
            user_orign_name = each_friend.NickName
            user_note = each_friend.RemarkName
            data_ea["user_id"] = user_id
            data_ea["user_orign_name"] = user_orign_name
            data_ea["user_note"] = user_note
            list_fin.append(data_ea)
            # print("发送信息的ID：", user_id)
            # print("好友自己的微信名字：", user_orign_name)
            # print("备注名字：", user_note)  # 搜索的

        msg = "查询成功"
    data_fin = {"status": 1, "msg": msg, "data": list_fin}
    logg(full_path, request.GET, data_fin)
    return Response(data_fin)


# 给好友发消息
@api_view(["POST"])
def send_to_friend(request):
    """
    通过 user_id 给好友发消息
    :param request: user_id，content
    demo: {
            "user_id":"",
            "content":"测试"
            }
    """

    full_path = request.get_full_path()
    data = request.data
    user_id = data.get("user_id")
    content = data.get("content")
    res = itchat.send(content, toUserName=user_id)
    print(res)
    res = res.get("BaseResponse").get("Ret")
    if res == 0:
        msg = "发送成功"
    elif res == -1:
        msg = "你查询的群组不存在！发送失败"
    else:
        msg = "发送失败"
    data_fin = {"status": 1, "msg": msg}
    logg(full_path, data, data_fin)
    return Response(data_fin)


# 二维码下载
@api_view(["GET"])
def big_file_download(request):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        # qrStorage.getvalue()
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = path_file
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'image/png'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response


@api_view(["GET"])
def reboot(request):
    # do something...

    import requests
    import itchat

    def get_response(_info):
        print(_info)  # 从好友发过来的消息
        api_url = 'http://www.tuling123.com/openapi/api'  # 图灵机器人接口地址
        data = {
            'key': 'f8a3234fc06743b4832087b0210dfc3e',  # 使用自己注册得到的key
            'info': _info,  # 这是我们从好友接收到的消息 然后转发给图灵机器人
            'userid': 'wechat-robot',
        }
        r = requests.post(api_url, data=data).json()  # 把data数据发
        print(r.get('text'))  # 机器人回复给好友的消息
        return r

    @itchat.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        return "【自动回复】" + "\n" + get_response(msg["Text"])["text"] + "\n" + "----------------" + "\n" + "From: ZH的机器人"


def insert_city(request):
    _list = []
    for each in city:
        _list.append(CITY(**each))
    CITY.objects.bulk_create(_list)
    return JsonResponse({"status": 1})
