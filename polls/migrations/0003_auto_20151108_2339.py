# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151108_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ousers',
            name='uEntryDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
