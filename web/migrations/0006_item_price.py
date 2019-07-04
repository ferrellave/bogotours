# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20190704_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.TextField(null=True, verbose_name='Price', blank=True),
        ),
    ]
