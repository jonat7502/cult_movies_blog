# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161115_1542'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]