# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-17 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0017_auto_20161017_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='mid',
        ),
        migrations.AddField(
            model_name='member',
            name='mid',
            field=models.IntegerField(null=True),
        ),
    ]