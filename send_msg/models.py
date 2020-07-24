from django.db import models


# Create your models here.
class WXGROUP(models.Model):
    group_name = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    operate_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'wx_group'


class CITY(models.Model):
    adcode = models.CharField(max_length=1024)
    citycode = models.CharField(max_length=1024)
    city_name = models.CharField(max_length=1024)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(max_length=12,default=1)

    class Meta:
        db_table = 'gd_city_map'
