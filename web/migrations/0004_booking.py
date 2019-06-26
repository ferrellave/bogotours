# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date', blank=True)),
                ('firstname', models.CharField(max_length=300, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=300, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=300, verbose_name='Phone')),
                ('email', models.CharField(max_length=300, verbose_name='Email')),
                ('tickets', models.IntegerField(verbose_name='Tickets', blank=True)),
                ('message', models.TextField(verbose_name='Message', blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('item', models.ForeignKey(verbose_name='Item', blank=True, to='web.Item', null=True)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
    ]
