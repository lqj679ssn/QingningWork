# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 10:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0004_timeline_is_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeline',
            old_name='related_writer',
            new_name='owner',
        ),
    ]
