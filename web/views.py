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
        context = super(booking, self).get_context_data(**kwargs)
        return context
    if request.method == 'POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            item = cleaned_data.get('item')
            date = cleaned_data.get('date')
            first = cleaned_data.get('first')
            last = cleaned_data.get('last')
            phone = cleaned_data.get('phone')
            tickets = cleaned_data.get('tickets')
            email = cleaned_data.get('email')
            message = cleaned_data.get('message')
            booking = Booking()
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
    else:
        form = Bookingform()
    context = {'form': form}
    context['item'] = Item.objects.all()
    return render(request, 'web/booking.html', context)

def signup_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('web.login'))
    def get_context_data(self, **kwargs):
        context = super(signup_view, self).get_context_data(**kwargs)
        return context
    if request.method == 'POST':
        form = signup_form(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')
            nickname = cleaned_data.get('nickname')
            user_model = User.objects.create_user(username=username, password=password)
            user_model.save()
            user_profile = UserProfile()
            user_profile.user = user_model
            user_profile.nickname = nickname
            user_profile.password2 = password2
            user_profile.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('web.home'), {'nickname': nickname})
                else:
                    pass
                message = 'Usuario incorrecto'
                return render(request, 'web/signup.html', {'message': message})
    else:
        form = signup_form()
    context = {'form': form}
    context['userprofile'] = UserProfile.objects.all()
    return render(request, 'web/signup.html', context)

def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('web.home'))
    message = ''
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    now = timezone.now()
    template = 'web/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('web.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                pass
        message = 'Invalid Email or Password. Try again'
    return render_to_response(template,locals(),context_instance=RequestContext(request))


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Ingresa para continuar')
    return redirect(reverse('app.login'))