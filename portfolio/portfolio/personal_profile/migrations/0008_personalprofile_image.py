# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0007_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
