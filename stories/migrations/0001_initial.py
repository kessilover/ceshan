# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-04 11:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_number', models.IntegerField(default=1, editable=False)),
                ('chapter', tinymce.models.HTMLField()),
                ('update_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('writer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=500)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('isCross', models.BooleanField(default=False)),
                ('first_fan', models.CharField(choices=[('CVG', 'جسور والجميلة'), ('KVS', ' ليث ونورا'), ('KG', 'عودة مهند'), ('Ezel', 'إيزل'), ('AM', 'العشق الممنوع'), ('MH', 'ميرنا وخليل'), ('GS', 'نور')], default=('KVS', ' ليث ونورا'), max_length=250)),
                ('second_fan', models.CharField(choices=[('CVG', 'جسور والجميلة'), ('KPA', 'العشق الأسود'), ('DA', '20 دقيقة'), ('GO', 'بائعة الورد'), ('Asi', 'عاصي'), ('IA', 'سنوات الضياع')], default=('KPA', 'العشق الأسود'), max_length=25)),
                ('rating', models.CharField(choices=[('k', 'K'), ('k+', 'K+'), ('t', 'T'), ('m', 'M')], default=('k+', 'K+'), max_length=3)),
                ('has_chapter', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story'),
        ),
    ]
