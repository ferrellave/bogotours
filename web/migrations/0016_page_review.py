# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_photo_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='review',
            field=models.TextField(verbose_name='Review', blank=True),
        ),
    ]
