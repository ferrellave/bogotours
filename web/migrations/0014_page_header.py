# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_profile_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='header',
            field=models.TextField(verbose_name='subtitulo', blank=True),
        ),
    ]
