# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Writer', '0003_auto_20170602_1401'),
        ('Work', '0004_auto_20170602_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='创建时间')),
                ('type', models.IntegerField(choices=[(0, '创建作品'), (1, '修改作品'), (2, '分享作品'), (3, '点赞作品'), (4, '评论作品')], verbose_name='时间线内容类型')),
                ('related_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Work.Work', verbose_name='关联作品')),
                ('related_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Writer.Writer', verbose_name='所属用户')),
            ],
        ),
    ]
