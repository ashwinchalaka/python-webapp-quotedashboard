# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-20 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteDash', '0003_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='liked_by',
            field=models.ManyToManyField(related_name='likesByUser', to='quoteDash.User'),
        ),
    ]