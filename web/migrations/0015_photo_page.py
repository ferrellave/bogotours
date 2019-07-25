# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_page_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='page',
            field=models.ForeignKey(verbose_name='page', blank=True, to='web.Page', null=True),
        ),
    ]
