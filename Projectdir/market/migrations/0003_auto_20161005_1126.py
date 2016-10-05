# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20161005_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockexchange',
            name='close',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='stockexchange',
            name='open',
            field=models.TimeField(),
        ),
    ]
