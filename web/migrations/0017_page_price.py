# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_page_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='price',
            field=models.CharField(default=0, max_length=300, verbose_name='Price'),
        ),
    ]
