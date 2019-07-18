# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_page_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='item',
            field=models.ForeignKey(related_name='item', blank=True, to='web.Item', null=True),
        ),
    ]
