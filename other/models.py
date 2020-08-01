from django.db import models

# Create your models here.


class QhLoveLog(models.Model):
    msg = models.CharField(max_length=2048)
    user_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'qh_log'