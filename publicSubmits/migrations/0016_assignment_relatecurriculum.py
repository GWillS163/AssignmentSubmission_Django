# Generated by Django 4.0.1 on 2022-02-24 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infoManage', '0002_alter_curriculum_id'),
        ('publicSubmits', '0015_remove_assignment_relatecurriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='relateCurriculum',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='infoManage.curriculum', verbose_name='所属课程'),
        ),
    ]
