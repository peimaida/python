# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20170322_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='password',
            field=models.TextField(max_length=5000),
        ),
    ]
