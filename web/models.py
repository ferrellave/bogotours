# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from django.conf import settings
import os
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    password2 = models.CharField(blank=True, max_length=200, verbose_name="Password")
    firstname = models.CharField(max_length=300, verbose_name="First Name")
    lastname = models.CharField(max_length=300, verbose_name="Last Name")
    phone = models.CharField(max_length=300, verbose_name="Phone")
    avatar = models.ImageField(upload_to='userprofiles/avatar', blank=True, null=True)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=True)
    class Meta:
        verbose_name = 'Userprofile'
        verbose_name_plural = 'Userprofiles'
    def __str__(self):
        return self.id
    def save(self):
        super(UserProfile, self).save()
        date = self.create_at
        self.slug = '%i-%i-%i-user-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(UserProfile, self).save()
        
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
    price = models.TextField(blank=True, null=True, verbose_name="Price")
    day = models.CharField(max_length=300, blank=True, null=True, verbose_name="Day")
    time = models.CharField(max_length=300, blank=True, null=True, verbose_name="Time")
    hours = models.CharField(max_length=300,  blank=True, null=True, verbose_name="Departure Time")
    recommendations = models.TextField(blank=True, null=True, verbose_name="Recommendations")
    important = models.TextField(blank=True, null=True, verbose_name="Important Information")
    departure = models.TextField(blank=True, null=True, verbose_name="Departure")
    returntime = models.TextField(blank=True, null=True, verbose_name="Return Time")
    included = models.TextField(blank=True, null=True, verbose_name="Included")
    notincluded = models.TextField(blank=True, null=True, verbose_name="Not Included")
    picture = models.ImageField(upload_to='items', blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Language")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Section")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Category")
    likes = models.IntegerField(blank=True, default=0, verbose_name="Likes")
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

class Booking(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Item")
    date = models.DateField(blank=True, verbose_name="Date")
    firstname = models.CharField(max_length=300, verbose_name="First Name")
    lastname = models.CharField(max_length=300, verbose_name="Last Name")
    phone = models.CharField(max_length=300, verbose_name="Phone")
    email = models.CharField(max_length=300, verbose_name="Email")
    tickets = models.IntegerField(blank=True, verbose_name="Tickets")
    message = models.TextField(blank=True, verbose_name="Message")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Booking"
        verbose_name_plural = 'Bookings'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Booking, self).save()
        date = self.created
        self.slug = '%i-%i-%i-booking-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(Booking, self).save()

class Page(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    ordering = models.IntegerField(blank=True, default=0, verbose_name="Ordering")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Page"
        verbose_name_plural = 'Pages'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

class Group(models.Model):
    first = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True, related_name="first")
    child = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True, related_name="child")
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Group"
        verbose_name_plural = 'Groups'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Group, self).save()
        date = self.created
        self.slug = '%i-%i-%i-group-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(Group, self).save()

class Profile(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True, related_name="page")
    description = models.TextField(blank=True, verbose_name="Description")
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Profile"
        verbose_name_plural = 'Profiles'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Profile, self).save()
        date = self.created
        self.slug = '%i-%i-%i-profile-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(Profile, self).save()
