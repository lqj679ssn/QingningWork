# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-12 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AbstractUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('abstractuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='AbstractUser.AbstractUser')),
                ('wid', models.AutoField(auto_created=True, db_index=True, editable=False, primary_key=True, serialize=False, verbose_name='作家编号')),
                ('total_works', models.IntegerField(default=0, verbose_name='全部投稿作品数')),
                ('total_received', models.IntegerField(default=0, verbose_name='被接纳的投稿作品数')),
                ('total_refused', models.IntegerField(default=0, verbose_name='被驳回的投稿作品数')),
                ('total_fee', models.FloatField(default=0, verbose_name='全部稿费')),
                ('remain_fee', models.FloatField(default=0, verbose_name='剩余稿费')),
                ('fee_method', models.CharField(default=None, max_length=50, verbose_name='文字描述获取稿费的方式')),
            ],
            bases=('AbstractUser.abstractuser',),
        ),
    ]