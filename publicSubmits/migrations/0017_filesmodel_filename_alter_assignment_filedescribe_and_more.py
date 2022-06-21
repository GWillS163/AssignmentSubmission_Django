# Generated by Django 4.0.1 on 2022-02-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicSubmits', '0016_assignment_relatecurriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesmodel',
            name='fileName',
            field=models.CharField(default=None, max_length=40, null=True, verbose_name='文件名'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='fileDescribe',
            field=models.CharField(blank=True, help_text='一般为.pdf .doc .docx 这些文件', max_length=20, null=True, verbose_name='文件要求'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='fileNameRule',
            field=models.CharField(blank=True, help_text='保留字(班级,学号,姓名)会被替换为学生信息', max_length=20, verbose_name='作业名规则'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, '按DDL自动判断'), (1, '尚未募集'), (2, '即将截止'), (3, '正在募集'), (4, '已经截止')], default=0, help_text='建议为默认值，过期则不收集。', verbose_name='作业状态'),
        ),
    ]