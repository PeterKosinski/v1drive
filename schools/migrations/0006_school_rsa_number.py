# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_school_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='rsa_number',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
    ]