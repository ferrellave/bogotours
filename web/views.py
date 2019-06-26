from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views import generic
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from .forms import FormularioContacto, Bookingform
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
    category = Category.objects.all().order_by('id')
    item = Item.objects.all().order_by('id')
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def us(request):

    template = 'web/us.html'
    category = Category.objects.all().order_by('id')
    item = Item.objects.all().order_by('id')
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))
def items(request):

    template = 'web/items.html'
    category = Category.objects.all().order_by('id')
    item = Item.objects.all().order_by('id')
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def item(request, slug):

    template = 'web/item.html'
    category = Category.objects.all().order_by('id')
    item = Item.objects.get(slug = slug)
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def itemgallery(request, slug):

    template = 'web/item-gallery.html'
    category = Category.objects.all().order_by('id')
    item = Item.objects.get(slug = slug)
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))


def blog(request, slug):

    template = 'web/blog.html'
    category = Category.objects.all().order_by('id')
    item = Item.objects.all().order_by('id')
    items = Item.objects.all().order_by('id')
    blogs = Blog.objects.get(slug = slug)
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def blogs(request):

    template = 'web/blogs.html'
    category = Category.objects.all().order_by('id')
    item = Item.objects.all().order_by('id')
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def contact(request):
    category = Category.objects.all().order_by('id')
    item = Item.objects.all().order_by('id')
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    if request.method =='POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            titulo = 'Thank You From Bogotours'
            correo = formulario.cleaned_data['correo']
            asunto = correo, 'Your Message to Bogotours has Send'
            mensaje = formulario.cleaned_data['mensaje']
            mail = EmailMessage(asunto, mensaje, to=[correo, 'richiepac@gmail.com'])
            mail.send()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'titulo': titulo})
    else:
        formulario = FormularioContacto()
    return render_to_response('web/contact.html', locals(),
                                context_instance=RequestContext(request))


def booking(request):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(booking, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = Bookingform(request.POST)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            cleaned_data = form.cleaned_data
            item = cleaned_data.get('item')
            date = cleaned_data.get('date')
            first = cleaned_data.get('first')
            last = cleaned_data.get('last')
            phone = cleaned_data.get('phone')
            tickets = cleaned_data.get('tickets')
            email = cleaned_data.get('email')
            message = cleaned_data.get('message')
            # E instanciamos un objeto User, con el username y password
        #    user_model = User.objects.create_user(username=username, password=password)
            # Y guardamos el objeto, esto guardara los datos en la db.
        #    user_model.save()
            # Ahora, creamos un objeto UserProfile
            booking = Booking()
            # Al campo user le asignamos el objeto user_model
           #track user_profile.user = user_model
            booking.date = date
            booking.item = item
            booking.firstname = first
            booking.lastname = last
            booking.phone = phone
            booking.email = email
            booking.message = message
            booking.tickets = tickets
            booking.save()
            messages = 'Booking success'
            return redirect(reverse('web.home'), {'messages': messages})
            # Ahora, redireccionamos a la pagina
            #user = authenticate(username=username, password=password)
            #if user is not None:
             #   if user.is_active:
              #      login(request, user)
               #     return redirect(reverse('app.welcome'), {'nickname': nickname})
                #else:
                    # Redireccionar informando que la cuenta esta inactiva
                 #   pass
                #message = 'Usuario incorrecto'
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = Bookingform()
    # Creamos el contexto
    context = {'form': form}
    context['item'] = Item.objects.all()
    # Y mostramos los datos
    return render(request, 'web/booking.html', context)
