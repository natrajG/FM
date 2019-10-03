# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-09-15 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20180503_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenditureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('amount', models.FloatField(default=0.0)),
                ('created_at', models.DateField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='bills',
            name='full_paid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='bills',
            name='penality',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bills',
            name='share_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bills',
            name='special_intrest',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bills',
            name='special_loan_amount',
            field=models.IntegerField(default=0),
        ),
    ]
