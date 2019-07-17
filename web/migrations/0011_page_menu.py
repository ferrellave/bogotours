# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20190717_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='menu',
            field=models.IntegerField(default=0, verbose_name='Menu', blank=True),
        ),
    ]
