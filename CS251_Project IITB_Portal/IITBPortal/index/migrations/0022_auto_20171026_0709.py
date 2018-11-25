# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_auto_20171026_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='all_students',
            field=models.ManyToManyField(default=None, to='index.Student'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='all_students',
            field=models.ManyToManyField(to='index.Student'),
        ),
    ]
