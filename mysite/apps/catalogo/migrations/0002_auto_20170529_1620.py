# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='fist_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='home_addres',
            new_name='home_address',
        ),
    ]
