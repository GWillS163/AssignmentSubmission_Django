# Generated by Django 4.0.1 on 2022-04-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManage', '0007_alter_userinfo_clazz_alter_userinfo_describe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='recentLoginTime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='最近登录'),
        ),
    ]
