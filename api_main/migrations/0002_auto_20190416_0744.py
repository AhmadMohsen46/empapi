# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-16 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
