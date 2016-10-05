# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('ceo', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Company2Exchange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=15)),
                ('stock_price', models.DecimalField(max_digits=12, decimal_places=2)),
                ('refresh_time', models.DateTimeField()),
                ('company', models.ForeignKey(to='market.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('short_name', models.CharField(max_length=15)),
                ('corp_tax_rate', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('symbol', models.CharField(max_length=5)),
                ('dollar_value', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55)),
                ('country', models.ForeignKey(to='market.Country')),
            ],
        ),
        migrations.CreateModel(
            name='StockExchange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('symbol', models.CharField(max_length=15)),
                ('open', models.DateTimeField()),
                ('close', models.DateTimeField()),
                ('headquarter', models.ForeignKey(to='market.Place')),
                ('primary_economy', models.ForeignKey(to='market.Country')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ForeignKey(to='market.Currency'),
        ),
        migrations.AddField(
            model_name='company2exchange',
            name='exchange',
            field=models.ForeignKey(to='market.StockExchange'),
        ),
        migrations.AddField(
            model_name='company',
            name='headquarter',
            field=models.ForeignKey(to='market.Place'),
        ),
    ]
