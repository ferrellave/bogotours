# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_page_paypal'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='currency',
            field=models.CharField(default=0, max_length=300, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='page',
            name='payinf',
            field=models.CharField(default=0, max_length=300, verbose_name='Payinf'),
        ),
    ]
