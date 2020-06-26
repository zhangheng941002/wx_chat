from django.db import models


# Create your models here.
class WXGROUP(models.Model):
    group_name = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    operate_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'wx_group'
