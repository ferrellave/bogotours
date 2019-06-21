# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.utils.timezone import now
import os
import datetime

class Categoria(models.Model):
    titulo = models.CharField(max_length=300, verbose_name="Titulo")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    foto = models.ImageField(upload_to='categorias', blank=True, null=True)
    numero = models.CharField(max_length=300, verbose_name="Numero",blank=True,null=True)
    creado = models.DateTimeField(default=now, editable=False)
    modificado = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['creado']
        verbose_name = "Servicio"
        verbose_name_plural = 'Servicios'

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Categoria, self).save(*args, **kwargs)

class Marca(models.Model):
    titulo = models.CharField(max_length=300, verbose_name="Titulo")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    foto = models.ImageField(upload_to='marcas', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Servicio")
    creado = models.DateTimeField(default=now, editable=False)
    modificado = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['creado']
        verbose_name = "Marca"
        verbose_name_plural = 'Marcas'

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Marca, self).save(*args, **kwargs)


class Producto(models.Model):
    titulo = models.CharField(max_length=300, verbose_name="Titulo")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    foto = models.ImageField(upload_to='productos', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Servicio")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, blank=True, null=True)
    creado = models.DateTimeField(default=now, editable=False)
    modificado = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['creado']
        verbose_name = "Producto"
        verbose_name_plural = 'Productos'

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Producto, self).save(*args, **kwargs)



class Blog(models.Model):
    titulo = models.CharField(max_length=300, verbose_name="Titulo")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    foto = models.ImageField(upload_to='productos', blank=True, null=True)
    creado = models.DateTimeField(default=now, editable=False)
    modificado = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['creado']
        verbose_name = "Blog"
        verbose_name_plural = 'Blogs'

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Blog, self).save(*args, **kwargs)