# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AbstractUser', '0006_auto_20170126_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractuser',
            name='introduce',
            field=models.CharField(default=None, max_length=20, verbose_name='一句话介绍'),
        ),
    ]