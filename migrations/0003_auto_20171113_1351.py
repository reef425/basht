# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basht', '0002_names_weather'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BashT',
        ),
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weather',
            name='vector',
            field=models.IntegerField(),
        ),
    ]
