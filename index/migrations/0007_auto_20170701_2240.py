# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20170701_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('communications_type', models.CharField(choices=[('\u4e1a\u52a1\u4ea4\u6d41', '\u4e1a\u52a1\u4ea4\u6d41'), ('\u6d3b\u52a8\u4ea4\u6d41', '\u6d3b\u52a8\u4ea4\u6d41')], max_length=10)),
                ('content', models.TextField()),
                ('submit_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Communicate',
        ),
    ]
