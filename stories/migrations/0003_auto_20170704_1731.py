# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-04 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20170704_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='chapter_text',
            new_name='chapter',
        ),
    ]
