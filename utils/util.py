class OPTList(object):

    # 求交集的两种方式
    def jiaoji(self, first, second):
        ret = list(set(first).intersection(set(second)))

        return ret

    # 求并集
    def bingji(self, first, second):
        ret = list(set(first).union(set(second)))
        return ret

    # 求差集，在second中但不在first中
    def chaji(self, first, second):
        ret = list(set(second).difference(set(first)))
        return ret


class OPTPhone(object):
    from phone import Phone

    def __init__(self):
        self.PHONE = OPTPhone.Phone()

    def find_phone(self, phone_num):
        """
        手机号归属地查询
        支持号段: 13*,15*,18*,14[5,7],17[0,6,7,8]
        :param phone_num:phone number
        :return:
                {
                    "phone": "15701350657",
                    "province": "北京",
                    "city": "北京",
                    "zip_code": "100000",
                    "area_code": "010",
                    "phone_type": "移动"
                }
        """
        return self.PHONE.find(phone_num)


class OPTFile(object):
    import os

    def __init__(self):
        self.os = OPTFile.os

    # 判断文件或者文件夹是否存在
    def file_exists(self, path):
        if self.os.path.exists(path):
            return True
        else:
            return False

    # 判断输入路径是文件还是文件夹
    def path_type(self, path):
        if self.os.path.isdir(path):
            # 文件夹
            print("it's a directory")
            return True, 1
        elif self.os.path.isfile(path):
            # 文件
            print("it's a normal file")
            return True, 2
        else:
            # 无效路径
            return False, 0

    # 获取文件大小
    def file_size(self, path):
        return self.os.path.getsize(path)

    # 获取文件下所有的文件和文件夹列表, 对于文件夹不在进一步检索
    def find_file_name(self, path, _type=1):

        status, code = OPTFile().path_type(path)
        if status and code == 1:
            if _type == 1:
                resp = self.os.listdir(path)
            else:
                filenames = self.os.listdir(path)
                for i in range(len(filenames)):
                    filenames[i] = path + filenames[i]

                resp = sorted(filenames)

            return True, resp
        else:
            return False, []

    # 范文路径下所有文件，如果是文件夹，则进去文件夹进行递归处理
    def find_all_file_name(self, path, _type=1):
        if _type == 1:
            resp = self.os.listdir(path)
        else:
            filenames = self.os.listdir(path)
            for i in range(len(filenames)):
                filenames[i] = path + filenames[i]

            resp = sorted(filenames)

        return resp


if __name__ == '__main__':
    diff = OPTList()
    a = [1, 2, 3, 4, 6]
    b = [2, 6, 7, 5, 8]
    print(diff.bingji(a, b))
    print(diff.chaji(a, b))
    print(diff.jiaoji(a, b))

    zh = OPTPhone()
    S = zh.find_phone("18911430184")
    print(S)

    file = OPTFile()
    path = '/home/zh/图片/wechat.jpg'

    print(file.file_exists(path))
    print(file.path_type(path))
    print(file.find_file_name(path))
    print(file.file_size(path))
