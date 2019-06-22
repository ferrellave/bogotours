from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views import generic
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from .forms import FormularioContacto
from .models import *

from django.contrib import messages 
from django.core.mail import send_mail, EmailMessage
from django.template import RequestContext
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest, HttpResponseRedirect
from django.core import serializers
import re
from django.db.models import Q
from django.core.context_processors import csrf
from django import forms 
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.utils.decorators import available_attrs, decorator_from_middleware


def home(request):

    template = 'web/home.html'
    blog = Blog.objects.all().order_by('-titulo')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def us(request):

    template = 'web/us.html'
    blog = Blog.objects.all().order_by('-titulo')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))
def items(request):

    template = 'web/items.html'
    blog = Blog.objects.all().order_by('-titulo')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def item(request):

    template = 'web/item.html'
    blog = Blog.objects.all().order_by('-titulo')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def blog(request):

    template = 'web/blog.html'
    blog = Blog.objects.all().order_by('-titulo')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def blogs(request):

    template = 'web/blogs.html'
    blog = Blog.objects.all().order_by('-titulo')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def contact(request):
    blog = Blog.objects.all().order_by('-titulo')
    if request.method =='POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            titulo = 'Gracias'
            correo = formulario.cleaned_data['correo']
            asunto = correo, 'Su mensaje ha sido enviado'
            mensaje = formulario.cleaned_data['mensaje']
            mail = EmailMessage(asunto, mensaje, to=[correo, 'webferrellave@gmail.com'])
            mail.send()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'titulo': titulo})
    else:
        formulario = FormularioContacto()
    return render_to_response('web/contact.html', locals(),
                                context_instance=RequestContext(request))