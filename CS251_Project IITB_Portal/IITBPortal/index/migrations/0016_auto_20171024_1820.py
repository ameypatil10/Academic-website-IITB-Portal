# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_auto_20171024_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(default='', max_length=100)),
                ('topic_info', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='parent_course',
        ),
        migrations.RemoveField(
            model_name='course_material',
            name='parent_course',
        ),
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
        migrations.AlterField(
            model_name='proff',
            name='email_id',
            field=models.EmailField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='email_id',
            field=models.EmailField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='topic',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='parent_topic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='index.Topic'),
        ),
        migrations.AddField(
            model_name='course_material',
            name='parent_topic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='index.Topic'),
        ),
    ]
