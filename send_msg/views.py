from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import itchat
import traceback
from django.http import StreamingHttpResponse

from yk_wx.setting_itchat import path_file
from .serializers import *

from .models import *
from django.http import JsonResponse
from utils.log_help import *

now_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)


@api_view(["GET"])
def check_IF_login(request):
    ourself_info = itchat.get_friends()
    if ourself_info:
        return Response({"status": 1, "msg": "微信已在线", "url": "http://www.zzhgod.com/"})
    else:

        return Response({"status": 1, "msg": "微信已不在线，请重新登录", "url": "http://www.zzhgod.com/"})


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
    """
    微信扫码登陆
    :param request:
    :return:
    """

    def get_response(info, remark_name):
        from qqai import TextChat

        siri = TextChat(settings.TX_KEY, settings.TX_TOKEN)
        answer = siri.ask(info)
        print("回复：", answer)
        MsgLog.objects.create(remark_name=remark_name, user_msg=info, reply_msg=answer)
        return answer

    @itchat.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        try:
            user = msg['User']
            print('---- 发送人 NickName：{}，备注：{} -------- 发送消息：{}'.format(user['NickName'], user['RemarkName'],
                                                                       msg['Text']))
            _msg = msg['Text']
            remark_name = user['RemarkName']
            if "关闭回复" in _msg:
                AutoChat.objects.filter(remark_name=remark_name, status=1).update(status=0)
            if "开启回复" in _msg:
                AutoChat.objects.filter(remark_name=remark_name, status=0).order_by("-id").update(status=1)
        except Exception as e:
            print(' !!!!!!!!!!!!! 发送错误-----', str(e))
            remark_name = str(e)

        if AutoChat.objects.filter(remark_name=remark_name, status=1).exists():
            _notice = AutoChatNotice.objects.filter(remark_name=remark_name, status=0)
            if _notice.exists():
                _notice.update(status=1)
                notice_msg = "\n\n" + "回复：关闭回复，则关闭智能对话；开启回复：则启动智能对话"
            else:
                notice_msg = ""
            return get_response(msg["Text"], remark_name) + notice_msg
        # return "【自动回复】" + "\n" + "我是机器人，不会聊天，请找主人说事"

    res = itchat.auto_login(hotReload=True)
    itchat.run()
    status = 1
    return Response({"status": status})


# 查询群组
@api_view(["GET"])
def get_group(request):
    """
    查询群组
    :param request: page_size,page_no,group_name
    demo:  /send_msg/get_group?group_name=测试1
    """

    group_name = request.GET.get("group_name", "")
    result = []

    if group_name:
        groups = itchat.search_chatrooms(name=group_name)
        print('--------------------------')
        print(groups)
        print('--------------------------')
        if groups:
            data = {}
            group = groups[0]
            data['UserName'] = group.get("UserName")
            data['NickName'] = group.get("NickName")
            data['MemberCount'] = group.get("MemberCount")
            data['MemberList'] = group.get("MemberList")
            result.append(data)
    else:
        groups = itchat.get_chatrooms(update=True)[1:]
        for each in groups:
            data = {}
            data['UserName'] = each.get("UserName")
            data['NickName'] = each.get("NickName")
            data['MemberCount'] = each.get("MemberCount")
            data['MemberList'] = each.get("MemberList")
            result.append(data)

    return Response({"status": 1, "results": result})


# 创建群组
@api_view(["POST"])
def create_group(request):
    """
    创建群组
    :param request: group_name,operator
    demo: {
            "group_name":"测试",
            "user_names": ["自己1", "自己2"],  # 创建群组要加入的成员（好友备注名）
            "first_msg": "新建的群组发送的第一条消息"  # 默认： hello everyone
            }
    """

    data = request.data
    group_name = data.get("group_name", None)
    user_names = data.get("user_names", None)
    first_msg = data.get("first_msg", settings.CREATE_GROUP_SEND_FIRST_MSG)
    if not isinstance(user_names, list):
        return Response({"status": 0, "msg": "user_names是列表形式！"})
    if len(user_names) < 2:
        return Response({"status": 0, "msg": "群组首次创建必须添加两个及以上成员！"})
    status = 1
    msg = "创建成功"
    member_list = []
    for name in user_names:
        member_list += itchat.search_friends(name=name)
    print(member_list)
    r = itchat.create_chatroom(member_list, group_name)

    print('------新建群组-------')
    print(r)
    print('-------------')
    try:
        if r.get("BaseResponse").get("Ret") != 0:
            status = 0
            msg = "创建失败"
        else:
            chat_root_name = r.get("ChatRoomName")
            itchat.send(first_msg, toUserName=chat_root_name)
    except:
        print(traceback.format_exc())
    data_fin = {"status": status, "msg": msg}
    return Response(data_fin)


# 向群组添加成员
@api_view(["POST"])
def add_user_to_group(request):
    """

    :param request:
    {
        "group_name": "测试群组2",
        "user_names": ["自己"],
    }
    :return:
    """

    status = 1
    msg = "添加成功"
    data = request.data
    group_name = data.get("group_name", None)  # 群组名称
    user_names = data.get("user_names", None)  # 要加入的好友, 列表形式，备注名称
    if not isinstance(user_names, list):
        return Response({"status": 0, "msg": "user_names是列表形式！"})
    if not user_names or not group_name:
        return Response({"status": 0, "msg": "user_names 和 group_name 不能为空"})
    chat_rooms = itchat.search_chatrooms(name=group_name)
    try:
        if not chat_rooms:
            status = 0
            msg = "没有查到群组"
            raise Exception(msg)
        group_id = ""
        for it in chat_rooms:
            print(it['NickName'])
            group_id = it["UserName"]
            break

        member_list = []
        for name in user_names:
            member_list += itchat.search_friends(name=name)

        if not member_list:
            status = 0
            msg = "没有查到你要添加的好友"
            raise Exception(msg)
        # 增加用户进入群聊
        res = itchat.add_member_into_chatroom(group_id, member_list)
        if res.get("BaseResponse").get("Ret") != 0:
            print(res)
            status = 0
            msg = "添加失败"
    except Exception as e:
        print(e)

    return Response({"status": status, "msg": msg})


# 给群组发消息
@api_view(["POST"])
def send_to_group(request):
    """
    :param request: group_name，content
    demo: {
            "group_name":"测试1",  # 模糊搜索， 仅支持保存到通讯录或者在调用该接口时群里有发送过消息的
            "content":"同名群组测试"
            }
    备注：该群组你需要先保存到通讯录才可以发送！

    """

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
    return Response(data_fin)


# 查询好友
@api_view(["GET"])
def get_friend(request):
    """
    查询好友
    :param request: friend_name
    demo: /send_msg/get_friend?friend_name=舒良松
    """

    friend_name = request.GET.get("friend_name", "")
    list_fin = []

    if friend_name:
        users = itchat.search_friends(name=friend_name)
        data = {}
        if users:
            user_id = users[0]['UserName']
            user_origin_name = users[0]['NickName']
            remark_name = users[0]['RemarkName']
            data["user_id"] = user_id
            data["user_origin_name"] = user_origin_name
            data["remark_name"] = remark_name
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
            user_origin_name = each_friend.NickName
            remark_name = each_friend.RemarkName
            data_ea["user_id"] = user_id
            data_ea["user_origin_name"] = user_origin_name
            data_ea["remark_name"] = remark_name
            list_fin.append(data_ea)

        msg = "查询成功"
    data_fin = {"status": 1, "msg": msg, "data": list_fin}
    # logg(full_path, request.GET, data_fin)
    return Response(data_fin)


# 给好友发消息
@api_view(["POST"])
def send_to_friend(request):
    """
    通过 user_id 给好友发消息
    :param request: user_id，content
    demo: {
            "username":"备注名",
            "content":"测试"
            }
    """

    data = request.data
    print('------------- send msg to your friend ----------', data)
    username = data.get("username")
    content = data.get("content")
    users = itchat.search_friends(name=username)
    status = 1
    if users:
        user_id = users[0]['UserName']
        res = itchat.send(content, toUserName=user_id)
        print(res)
        res = res.get("BaseResponse").get("Ret")
        if res == 0:
            msg = "发送成功"
        elif res == -1:
            msg = "你查询的群组不存在！发送失败"
            status = 0
        else:
            msg = "发送失败"
            status = 0
    else:
        msg = "没有查找到你的好友~"
        status = 0
    data_fin = {"status": status, "msg": msg}
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


# 默认将所有有备注的好友加入自动回复
@api_view(["POST"])
def auto_add_chat(request):
    """
    默认将所有有备注的好友加入自动回复
    :param request: {
                "names": ["自己1", "自己2"]  # 数组形式
        }
    demo:
    """
    data = request.data
    names = data.get("names", None)
    if names:
        if not isinstance(names, list):
            return Response({"status": 0, "msg": "names是list类型！"})
    friend_list = itchat.get_friends()[1:]
    all_list = []
    notice_list = []
    _data = []
    if names:
        for name in names:
            users = itchat.search_friends(name=name)
            data = {}
            if users:
                data_ea = {}
                user_id = users[0]['UserName']
                user_origin_name = users[0]['NickName']
                remark_name = users[0]['RemarkName']
                data["user_id"] = user_id
                data["user_origin_name"] = user_origin_name
                data["remark_name"] = remark_name
                _data.append(data_ea)
                all_list.append(AutoChat(remark_name=remark_name))
                notice_list.append(AutoChatNotice(remark_name=remark_name))
    else:
        for each_friend in friend_list:
            data_ea = {}
            user_id = each_friend.UserName
            user_origin_name = each_friend.NickName
            remark_name = each_friend.RemarkName
            data_ea["user_id"] = user_id
            data_ea["user_origin_name"] = user_origin_name
            data_ea["remark_name"] = remark_name
            if remark_name:
                if not AutoChat.objects.filter(remark_name=remark_name, status=1).exists():
                    _data.append(data_ea)
                    all_list.append(AutoChat(remark_name=remark_name))
                    notice_list.append(AutoChatNotice(remark_name=remark_name))

    if all_list:
        AutoChat.objects.bulk_create(all_list)
        AutoChatNotice.objects.bulk_create(notice_list)

    msg = "添加成功"
    data_fin = {"status": 1, "msg": msg, "data": _data}
    return Response(data_fin)


# 取消好友自动回复
@api_view(["POST"])
def auto_del_chat(request):
    """
    取消好友自动回复
    :param request:
            ｛
                "names": ["自己1", "自己2"]  # 数组形式
            ｝
    demo:
    """

    data = request.data
    names = data.get("names")
    print('---------------', data)
    for name in names:
        AutoChat.objects.filter(remark_name=name, status=1).update(status=0)
    msg = "取消成功"
    data_fin = {"status": 1, "msg": msg}
    return Response(data_fin)


def insert_data(request):
    _list = []
    _data = []
    for each in _data:
        _list.append(QhLove(**each))
    QhLove.objects.bulk_create(_list)
    return JsonResponse({"status": 1})
