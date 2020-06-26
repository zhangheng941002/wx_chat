# wx msg Dockerfile

FROM python:3.6.8

WORKDIR /yk_wx

ADD requirement.txt /requirement.txt
RUN pip install -U -r /requirement.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
