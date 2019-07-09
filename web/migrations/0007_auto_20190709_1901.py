# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0006_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password2', models.CharField(max_length=200, verbose_name='Password', blank=True)),
                ('firstname', models.CharField(max_length=300, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=300, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=300, verbose_name='Phone')),
                ('avatar', models.ImageField(null=True, upload_to='userprofiles/avatar', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Userprofile',
                'verbose_name_plural': 'Userprofiles',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Likes', blank=True),
        ),
    ]
