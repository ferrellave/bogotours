# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.utils.timezone import now
import os
import datetime

class Language(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    picture = models.ImageField(upload_to='Language', blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Language"
        verbose_name_plural = 'Languages'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Language, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to='categories', blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Language")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Category"
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Section(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to='sections', blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Language")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Category")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Section"
        verbose_name_plural = 'Sections'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Section, self).save(*args, **kwargs)

class Item(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to='items', blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Language")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Section")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Category")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Item"
        verbose_name_plural = 'Items'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)

class Tag(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to='blogs', blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Language")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Tag"
        verbose_name_plural = 'Tags'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to='blogs', blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Language")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Tag")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Blog"
        verbose_name_plural = 'Blogs'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

class Photo(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    file = models.ImageField(upload_to='photos', blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Item")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Blog")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Photo"
        verbose_name_plural = 'Photos'

    def __unicode__(self):
        return self.title

    def save(self):
        super(Photo, self).save()
        date = self.created
        self.slug = '%i-%i-%i-photo-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(Photo, self).save()