from django.db import models


# Create your models here.
class WXGROUP(models.Model):
    group_name = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    operate_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'wx_group'


class CITY(models.Model):
    pid = models.IntegerField(max_length=12)
    city_code = models.CharField(max_length=1024)
    city_name = models.CharField(max_length=1024)
    post_code = models.CharField(max_length=1024)
    area_code = models.CharField(max_length=1024)
    ctime = models.DateTimeField()

    class Meta:
        db_table = 'city'
