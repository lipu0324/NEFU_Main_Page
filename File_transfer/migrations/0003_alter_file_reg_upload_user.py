# Generated by Django 4.0.5 on 2022-07-07 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('File_transfer', '0002_alter_file_reg_recieve_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_reg',
            name='Upload_user',
            field=models.CharField(max_length=256, null=True),
        ),
    ]