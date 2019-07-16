# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20190716_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('photo', models.ImageField(null=True, upload_to='photos', blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('page', models.ForeignKey(related_name='page', blank=True, to='web.Page', null=True)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
