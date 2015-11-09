# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=100, null=True)),
                ('lastNme', models.CharField(max_length=100, null=True)),
                ('lastLogin', models.DateTimeField(null=True)),
                ('isLoggedIn', models.BooleanField(default=False)),
            ],
        ),
    ]
