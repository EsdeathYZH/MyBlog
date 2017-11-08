# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-publish_date',),
            },
        ),
    ]
