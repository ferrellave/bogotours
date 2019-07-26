# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_page_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='paypal',
            field=models.TextField(verbose_name='Paypal', blank=True),
        ),
    ]
