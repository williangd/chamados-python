# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='problema',
            field=models.TextField(blank=True, null=True),
        ),
    ]