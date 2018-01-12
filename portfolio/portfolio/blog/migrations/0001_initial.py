# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=255)),
                ('b_content', models.TextField()),
                ('b_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
