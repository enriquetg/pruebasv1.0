# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_person_creado'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos_media'),
            preserve_default=False,
        ),
    ]