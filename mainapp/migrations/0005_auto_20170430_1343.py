# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20170430_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psyptitemdef',
            name='keyed',
            field=models.TextField(default='+'),
        ),
    ]
