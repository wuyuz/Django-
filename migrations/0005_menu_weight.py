# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-15 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20190712_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='weight',
            field=models.IntegerField(default=1),
        ),
    ]