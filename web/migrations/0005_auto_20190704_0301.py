# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_booking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['created'], 'verbose_name': 'Booking', 'verbose_name_plural': 'Bookings'},
        ),
        migrations.AddField(
            model_name='item',
            name='day',
            field=models.CharField(max_length=300, null=True, verbose_name='Day', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='departure',
            field=models.TextField(null=True, verbose_name='Departure', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='hours',
            field=models.CharField(max_length=300, null=True, verbose_name='Departure Time', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='important',
            field=models.TextField(null=True, verbose_name='Important Information', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='included',
            field=models.TextField(null=True, verbose_name='Included', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='notincluded',
            field=models.TextField(null=True, verbose_name='Not Included', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='recommendations',
            field=models.TextField(null=True, verbose_name='Recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='returntime',
            field=models.TextField(null=True, verbose_name='Return Time', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.CharField(max_length=300, null=True, verbose_name='Time', blank=True),
        ),
    ]
