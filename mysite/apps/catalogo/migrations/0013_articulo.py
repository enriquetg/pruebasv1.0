# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0012_auto_20170610_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('contenido', models.TextField(blank=True)),
                ('state', models.CharField(choices=[('1', 'Publico'), ('2', 'Privado')], max_length=10)),
                ('creado', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro', verbose_name='Fecha de creacion')),
                ('photo', models.ImageField(null=True, upload_to='Articulo_photos_media')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Person')),
            ],
        ),
    ]
