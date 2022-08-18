from django.db import models


# Create your models here.
class File_reg(models.Model):
    # 创建主键名称是File_id
    File_id = models.CharField(primary_key=True, max_length=40)
    File_name = models.CharField(max_length=100)
    File_path = models.CharField(max_length=100)
