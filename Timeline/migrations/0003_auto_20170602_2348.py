# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0002_auto_20170602_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='create_time',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name='创建时间'),
        ),
    ]