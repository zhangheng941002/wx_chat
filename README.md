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

### 二、项目运行、部署

#### 1、调试可使用`runserver`

```shell
python manage.py runserver 0.0.0.0:8000
```

#### 2、生产部署建议使用`Uwsgi`+`Nginx`

```shell
uwsgi --http 0.0.0.0:8000 --chdir /code/ --wsgi-file /code/yk_wx/wsgi.py --module yk_wx.wsgi --master --processes 8 --threads 4
```

备注：上面的文件路径请自行修改

#### 3、使用docker进行服务部署

##### （1）生成镜像

```
docker build -t wx:v1 .
```

##### （2）启动服务，二选一即可

###### ① 使用`uwsgi`启动服务

```
docker run -idt -v /data/wx_chat:/code -p 127.0.0.1:8000:8000  --name=wx wx:v1 uwsgi --http 0.0.0.0:8000 --chdir /code/ --wsgi-file /code/yk_wx/wsgi.py --module yk_wx.wsgi --master --processes 8 --threads 4
```

###### ② 使用`runserver`启动服务

```shell
docker run -idt -v /data/wx_chat:/code -p 127.0.0.1:8000:8000  --name=wx wx:v1
```

### 三、目前实现功能

#### 1、微信相关

##### （1）微信登录

##### （2）退出微信

##### （3）获取微信好友列表

##### （4）给指定好友发送消息

##### （5）给指定好友发送指定城市的天气，默认3天

备注：

​		默认开启自动回复，可关闭，修改`settings.py`文件中AUTO_CHAT=False即可关闭自动回复

#### 2、其他

##### （1）获取指定城市（区）天气
##### （2）获取IP地址
备注：
        默认查询访问主机IP，只支持国内IP，如果在局域网 IP网段内，则返回“局域网”；非法IP以及国外IP则返回空
##### （3）手机号归属地查询
        
### 四、搭建FTP服务器
```
python manage.py run_ftp_server
```