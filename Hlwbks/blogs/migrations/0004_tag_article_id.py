# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-13 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20190213_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='article_id',
            field=models.ManyToManyField(to='blogs.Article', verbose_name='所属博客'),
        ),
    ]