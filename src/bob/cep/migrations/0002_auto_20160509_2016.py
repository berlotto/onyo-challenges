# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cep',
            name='cep',
            field=models.BigIntegerField(),
        ),
    ]