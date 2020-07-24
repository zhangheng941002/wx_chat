#!/usr/bin/python
# coding=utf-8
import os
from ftplib import FTP


class MyFtp(object):
    ftp = FTP()

    def __init__(self, host,username, password, port=21):
        self.ftp.connect(host, port)
        self.ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
        self.ftp.login(username, password)
        print(self.ftp.welcome)  # 打印出欢迎信息

    # 上传文件
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

    # 下载文件
    def download_file(self, local_path, remote_path, filename):
        """
        下载文件
        :param local_path: 本地文件的路径
        :param remote_path: 服务器的路径
        :param filename: 下载的文件的名称
        :return:
        """
        os.chdir(local_path)  # 切换工作路径到下载目录
        self.ftp.cwd(remote_path)  # 要登录的ftp目录
        self.ftp.nlst()  # 获取目录下的文件
        file_handle = open(filename, "wb").write  # 以写模式在本地打开文件
        self.ftp.retrbinary('RETR %s' % os.path.basename(filename), file_handle, blocksize=1024)  # 下载ftp文件

    # 删除文件
    def delete_file(self, remote_file):
        """
        删除
        :param remote_file: 删除的服务器上的路径+文件名称
        :return:
        """
        self.ftp.delete(remote_file)

    # 显示目录下所有目录信息
    def get_dirs(self):
        return self.ftp.dir()

    # 设置FTP当前操作的路径
    def pwd(self):
        return self.ftp.pwd()

    # 返回一个文件名列表
    def filename_list(self):
        return self.ftp.nlst()

    # 设置FTP当前操作的路径
    def set_opt_path(self, path):
        """
        :param path:
        :return:
        """
        return self.ftp.cwd(path)

    # 新建远程目录
    def mkdir(self, file_name):
        """
        :param file_name:
        :return:
        """
        return self.ftp.mkd(file_name)

    # 删除远程目录,只能删除空文件夹
    def rmdir(self, dir_name):
        """
        :param dir_name:
        :return:
        """
        self.set_opt_path(dir_name)
        for i in self.filename_list():
            print('------------ 删除远程目录：{}下文件：{}'.format(dir_name, i))
            self.delete_file(i)
        self.ftp.cwd("..")
        return self.ftp.rmd(dir_name)

    # 修改文件夹或文件名称
    def rename(self, old_name, new_name):
        """
        :param old_name:
        :param new_name:
        :return:
        """
        return self.ftp.rename(old_name, new_name)

    # 关闭调试
    def close(self):
        self.ftp.set_debuglevel(0)
        self.ftp.quit()


if __name__ == '__main__':
    ftp = MyFtp('172.30.41.20','user', '12345')
    # ftp = MyFtp('172.31.0.9')
    # ftp.login('user', '12345')
    # ftp.downloadFile('/home/zh/桌面/myself/myself', '/test', 'wlj-test.rar')

    # ftp.upload_file('/home/zh/文档/服务器出错页面.zip', '/test/wlj-upload.zip')

    """
    删除
    """
    # print(ftp.get_dirs())
    # ftp.delete_file('/id_rsa')

    # ftp.mkdir("zh1")
    # ftp.upload_file(r"C:/Users/zh/.ssh/id_rsa", '/zh1/id_rsa')
    # ftp.set_opt_path("/zh1")
    # print(ftp.filename_list())

    # ftp.rename("id_rsa", "id_ras_new")
    ftp.rmdir("zh1")
    # print(ftp.filename_list())
    ftp.close()
