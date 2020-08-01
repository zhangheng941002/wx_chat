### 一、项目介绍

#### 1、使用语言

```
python:3.x
```

#### 2、使用框架

```
Django==2.0.6
```

#### 3、使用主要三方依赖

```
itchat（对开源代码进行修改）
qqai==0.2.1(自动回复)
```

#### 4、运行环境

```
Windows 和 Linux 都可运行
```

### 二、项目运行

#### 1、安装依赖

```
pip install -r requirement.txt
```

#### 2、更改配置信息

##### ① `settings.py`相关信息修改

```
#数据库配置，更换成你自己的
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wx',  # 数据库
        'USER': 'root',  # 用户
        'HOST': '127.0.0.1',  # IP
        'PORT': '3306',  # 端口
        'PASSWORD': '123456',  # 密码
        'CHARSET': 'UTF8'
    }

}
```

##### ② 生成数据库相关表

```
python manage.py makemigrations send_msg

python manage.py migrate
```

##### ③ 插入相关数据

```
在数据库中执行db_sql下的两个sql文件
```



#### 2、本地调试，以下方式二选一即可

##### ①`runserver`

```shell
python manage.py runserver 0.0.0.0:8000
```

##### ②`Uwsgi`

```shell
uwsgi --http 0.0.0.0:8000 --wsgi-file yk_wx/wsgi.py --module yk_wx.wsgi --master --processes 8 --threads 4
```

备注：上面的文件路径请自行修改

### 三、生产环境部署

#### 1、使用docker进行服务部署

##### （1）生成镜像

```
# 如果不指定Dockerfile路径，需要在Dockerfile文件所在的同级目录下执行
docker build -t wx:v1 .
```

##### （2）启动服务，二选一即可，建议使用`uwsgi`

###### ① 使用`uwsgi`启动服务

```
docker run -idt -v /data/wx_chat:/code -p 127.0.0.1:8000:8000  --name=wx wx:v1 uwsgi --http 0.0.0.0:8000 --chdir /code/ --wsgi-file /code/yk_wx/wsgi.py --module yk_wx.wsgi --master --processes 8 --threads 4
```

###### ② 使用`runserver`启动服务

```shell
docker run -idt -v /data/wx_chat:/code -p 127.0.0.1:8000:8000  --name=wx wx:v1
```

### 四、目前实现功能

#### 1、微信相关

##### （1）微信登录

##### （2）退出微信

##### （3）获取微信好友列表

##### （4）给指定好友发送情话

##### （5）给指定好友发送消息

##### （6）给指定好友发送指定城市的天气，默认3天

##### （7）增加自动回复定制化
```
针对已添加备注的好友，设置自动回复，好友可自动关闭/开启自动回复
```

##### （8）获取保存到通讯录的群组

##### （9）创建群组

##### （10）将好友拉入群组

##### （11）向群组发送消息

`备注：微信好友相关操作，仅限于有备注的好友`

#### 2、其他

##### （1）获取指定城市（区）天气
##### （2）获取IP地址
备注：
        默认查询访问主机IP，只支持国内IP，如果在局域网 IP网段内，则返回“局域网”；非法IP以及国外IP则返回空
##### （3）手机号归属地查询

### 五、搭建FTP服务器
```
python manage.py run_ftp_server
```
