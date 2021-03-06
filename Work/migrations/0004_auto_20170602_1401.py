# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0003_auto_20170123_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='create_time',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='work',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '正在创作'), (1, '正在审稿'), (2, '审稿通过，商讨稿费'), (3, '审稿驳回'), (4, '确认稿费')], default=0, verbose_name='作品状态'),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_type',
            field=models.SmallIntegerField(choices=[(0, '纯文本'), (1, '文件'), (2, '音乐')], default=0, verbose_name='作品类型'),
        ),
    ]
