# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='none'),
            preserve_default=False,
        ),
    ]
