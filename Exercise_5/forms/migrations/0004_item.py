# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20170509_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit_of_measurement', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('purpose', models.CharField(max_length=100)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Document')),
            ],
        ),
    ]