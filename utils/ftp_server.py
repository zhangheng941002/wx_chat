#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/7/24 11:39
# @Author : Zh
# @Project : yk_wx
# @File   : run_ftp_server.py
# @Software: PyCharm
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from django.conf import settings


def ftp_server_run(ip=settings.FTP_CONFIG["IP"], username=settings.FTP_CONFIG["USERNAME"],
                   file_path=settings.FTP_CONFIG["FILE_PATH"], password=settings.FTP_CONFIG["PASSWORD"],
                   port=settings.FTP_CONFIG["PORT"], max_cons=settings.FTP_CONFIG["MAX_CONS"],
                   max_cons_per_ip=settings.FTP_CONFIG["MAX_CONS_PER_IP"]):
    # 实例化DummyAuthorizer来创建ftp用户
    authorizer = DummyAuthorizer()
    # 参数：用户名，密码，目录，权限
    authorizer.add_user(username, password, file_path, perm='elradfmwMT')
    # 匿名登录
    # authorizer.add_anonymous('/home/nobody')

    handler = FTPHandler
    handler.authorizer = authorizer

    # 参数：IP，端口，handler
    server = FTPServer((ip, port), handler)
    server.max_cons = max_cons
    server.max_cons_per_ip = max_cons_per_ip

    server.serve_forever()

    """
    perm权限选项
        读取权限：
        
        "e" =更改目录（CWD，CDUP命令）
        "l" =列表文件（LIST，NLST，STAT，MLSD，MLST，SIZE命令）
        "r" =从服务器检索文件（RETR命令）
        写入权限：
        
        "a" =将数据追加到现有文件（APPE命令）
        "d" =删除文件或目录（DELE，RMD命令）
        "f" =重命名文件或目录（RNFR，RNTO命令）
        "m" =创建目录（MKD命令）
        "w" =将文件存储到服务器（STOR，STOU命令）
        "M"=更改文件模式/权限（SITE CHMOD命令）
        "T"=更改文件修改时间（SITE MFMT命令）

    """


if __name__ == '__main__':
    pass
