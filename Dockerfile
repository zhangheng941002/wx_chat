# wx msg Dockerfile

FROM python:3.6.8

WORKDIR /yk_wx

ADD requirement.txt /requirement.txt
RUN pip install -U -r /requirement.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

## 生成镜像
# docker build -t yk_wx:12.13 .

## 创建容器
# docker run -it -v /data/yk_wx:/yk_wx -p 0.0.0.0:13000:8000  --name=yk_wx yk_wx:12.13
