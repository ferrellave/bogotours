# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_profile_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='header',
            field=models.TextField(verbose_name='subtitulo', blank=True),
        ),
    ]
