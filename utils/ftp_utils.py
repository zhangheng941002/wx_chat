#!/usr/bin/python
# coding=utf-8
import os
from ftplib import FTP


class MyFtp():
    ftp = FTP()

    def __init__(self, host, port=21):
        self.ftp.connect(host, port)

    def login(self, username, pwd):
        self.ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
        self.ftp.login(username, pwd)
        print(self.ftp.welcome)

    def downloadFile(self, localpath, remotepath, filename):
        """
        下载文件
        :param localpath: 本地文件的路径
        :param remotepath: 服务器的路径
        :param filename: 下载的文件的名称
        :return:
        """
        os.chdir(localpath)  # 切换工作路径到下载目录
        self.ftp.cwd(remotepath)  # 要登录的ftp目录
        self.ftp.nlst()  # 获取目录下的文件
        file_handle = open(filename, "wb").write  # 以写模式在本地打开文件
        self.ftp.retrbinary('RETR %s' % os.path.basename(filename), file_handle, blocksize=1024)  # 下载ftp文件

    def upload_file(self, local_file, remote_file):
        """
        上传
        :param local_file: 本地文件路径+文件名称
        :param remote_file: 服务器上的路径+文件名称
        :return:
        """
        buf_size = 1024
        file_handler = open(local_file, 'rb')
        self.ftp.storbinary('STOR %s' % remote_file, file_handler, buf_size)
        file_handler.close()

    def delete_file(self, remote_file):
        """
        删除
        :param remote_file: 删除的服务器上的路径+文件名称
        :return:
        """
        self.ftp.delete(remote_file)

    def close(self):
        self.ftp.set_debuglevel(0)  # 关闭调试
        self.ftp.quit()


if __name__ == '__main__':
    ftp = MyFtp('172.31.0.9')
    ftp.login('user', '12345')
    # ftp.downloadFile('/home/zh/桌面/myself/myself', '/test', 'wlj-test.rar')

    # ftp.upload_file('/home/zh/文档/服务器出错页面.zip', '/test/wlj-upload.zip')

    """
    删除
    """
    ftp.delete_file('/test/wlj-upload-1575281420.9298873.zip')
    ftp.close()
