# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-15 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AbstractUser', '0003_auto_20170115_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractuser',
            name='login_times',
            field=models.IntegerField(default=0, verbose_name='登录次数'),
        ),
    ]
