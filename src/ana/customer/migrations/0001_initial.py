# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('zipcode', models.BigIntegerField()),
                ('street', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
    ]
