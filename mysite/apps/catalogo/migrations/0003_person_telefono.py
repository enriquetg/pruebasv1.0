# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 21:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20170529_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='telefono',
            field=models.CharField(default=datetime.datetime(2017, 5, 29, 16, 25, 48, 278462), max_length=12),
            preserve_default=False,
        ),
    ]