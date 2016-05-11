# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=1000)),
                ('cidade', models.CharField(max_length=500)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]