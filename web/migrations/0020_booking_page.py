# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20190726_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='page',
            field=models.ForeignKey(verbose_name='Page', blank=True, to='web.Page', null=True),
        ),
    ]
