from django.db import models

# Create your models here.
class File_reg(models.Model):
    #创建主键名称是File_id
    File_id = models.AutoField(primary_key=True)
    File_name = models.CharField(max_length=100)
    File_path = models.CharField(max_length=100)
    Upload_time = models.DateTimeField(auto_now_add=True)
    Upload_user = models.CharField(max_length=256,null=True)
    Recieve_user = models.CharField(max_length=256)
    Encryption_status = models.BooleanField(default=False)