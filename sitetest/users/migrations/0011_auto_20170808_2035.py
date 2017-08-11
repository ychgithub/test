# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-08 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_usertest_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertest',
            name='markdown_or_not',
        ),
        migrations.AddField(
            model_name='usertest',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='usertest',
            name='user_sex',
            field=models.CharField(choices=[('man', '男'), ('woman', '女'), ('futa', '小姐姐')], default='futa', max_length=10, verbose_name='性别'),
        ),
    ]