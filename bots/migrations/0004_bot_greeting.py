# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0003_auto_20171126_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='greeting',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]