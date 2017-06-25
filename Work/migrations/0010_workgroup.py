# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-25 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0009_remove_work_work_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Work.Work', unique=True, verbose_name='最新稿')),
            ],
        ),
    ]