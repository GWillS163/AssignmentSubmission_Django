# Generated by Django 4.0.1 on 2022-03-02 08:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoManage', '0002_alter_curriculum_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userManage', '0004_professor_student_delete_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student',
            new_name='userInfo',
        ),
        migrations.DeleteModel(
            name='professor',
        ),
    ]
