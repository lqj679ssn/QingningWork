# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0002_auto_20170123_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='version_num',
            field=models.IntegerField(default=1, verbose_name='作品第几版'),
        ),
    ]
