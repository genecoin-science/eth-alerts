# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170221_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='abi',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alert',
            name='delete_key',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]