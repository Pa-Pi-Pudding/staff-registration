# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comike', '0009_auto_20170831_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier_shift', models.IntegerField(choices=[(0, '雨'), (1, '晴')], default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='information',
            name='carrier_shift',
        ),
    ]
