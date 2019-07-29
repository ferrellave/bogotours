from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views import generic
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from .forms import FormularioContacto, Bookingform, signup_form
from .models import *

from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

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
from django.utils import timezone

from ipware import get_client_ip

def home(request):

    template = 'web/home.html'
    category = Category.objects.all().order_by('id')
    item = Item.objects.all().order_by('id')
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    groups = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
    profilem = Profile.objects.all()[:7]
    profiles = Profile.objects.all().order_by('-id')
    profilesn = Profile.objects.all().order_by('-id')
    client_ip, is_routable = get_client_ip(request)
    return render_to_response(template,locals(),
                                context_instance=RequestContext(request))

def page(request, slug):

    template = 'web/page.html'
    link = Page.objects.get(slug = slug)
    category = Category.objects.all().order_by('id')
    item = Item.objects.all().order_by('id')
    items = Item.objects.all().order_by('id')
    section = Section.objects.all().order_by('id')
    photo = Photo.objects.all().order_by('id')
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all().order_by('-id')
    pages = Page.objects.all().order_by('ordering')
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    groups = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
    profiles = Profile.objects.all().order_by('-id')
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
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
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
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
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
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
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
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
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
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
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
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
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
    page = Page.objects.all().order_by('ordering')
    group = Group.objects.all().order_by('-id')
    profile = Profile.objects.all().order_by('-id')
    if request.method =='POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            titulo = 'Thank You From Bogotours'
            correo = formulario.cleaned_data['correo']
            asunto = correo, 'Your Message to Bogotours has Send'
            mensaje = formulario.cleaned_data['mensaje']
            mail = EmailMessage(asunto, mensaje, to=[correo, 'richiepac@gmail.com', 'bogotourstravel@gmail.com'])
            mail.send()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'titulo': titulo})
    else:
        formulario = FormularioContacto()
    return render_to_response('web/contact.html', locals(),
                                context_instance=RequestContext(request))

def booking(request, slug):
    def get_context_data(self, **kwargs):
        context = super(booking, self).get_context_data(**kwargs)
        context['tour'] = Page.objects.get(slug = slug)
        context['photo'] = Photo.objects.all().order_by('id')
        context['blog'] = Blog.objects.all().order_by('-id')
        context['tag'] = Tag.objects.all().order_by('-id')
        context['page'] = Page.objects.all().order_by('ordering')
        context['pages'] = Page.objects.all().order_by('ordering')
        context['group'] = Group.objects.all().order_by('-id')
        context['groups'] = Group.objects.all().order_by('-id')
        context['profile'] = Profile.objects.all().order_by('-id')
        context['profiles'] = Profile.objects.all().order_by('-id')
        return context
    if request.method == 'POST':
        form = Bookingform(request.POST)
        context['tour'] = Page.objects.get(slug = slug)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            date = cleaned_data.get('date')
            first = cleaned_data.get('first')
            last = cleaned_data.get('last')
            phone = cleaned_data.get('phone')
            tickets = cleaned_data.get('tickets')
            email = cleaned_data.get('email')
            message = cleaned_data.get('message')
            booking = Booking()
            booking.date = date
            booking.page = tour
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
    context['tour'] = Page.objects.get(slug = slug)
    context['photo'] = Photo.objects.all().order_by('id')
    context['blog'] = Blog.objects.all().order_by('-id')
    context['tag'] = Tag.objects.all().order_by('-id')
    context['page'] = Page.objects.all().order_by('ordering')
    context['pages'] = Page.objects.all().order_by('ordering')
    context['group'] = Group.objects.all().order_by('-id')
    context['groups'] = Group.objects.all().order_by('-id')
    context['profile'] = Profile.objects.all().order_by('-id')
    context['profiles'] = Profile.objects.all().order_by('-id')
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
            firstname = cleaned_data.get('firstname')
            user_model = User.objects.create_user(username=username, password=password)
            user_model.save()
            user_profile = UserProfile()
            user_profile.user = user_model
            user_profile.firstname = firstname
            user_profile.password2 = password2
            user_profile.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('web.booking'), {'firstname': firstname})
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
        return redirect(reverse('web.booking'))
    message = ''
    now = timezone.now()
    template = 'web/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('web.booking'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                pass
        message = 'Mail o password invalido'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    messages.success(request, 'Ingresa para continuar')
    return redirect(reverse('web.login'))