from django.conf.urls import url
# -*- encoding: utf-8 -*-
from . import views

urlpatterns = [
    # /blog/ | /
 #   url(r'^$', views.ArticleListView.as_view(), name='blog.article_list'),
 #   url(r'^@(?P<slug>[-\w]+)/$', 'blog.views.UserProfileDetailView', name='blog.userprofile_detail'),
  #  url(r'^publicacion/(?P<slug>[^\.]+)/$', 'blog.views.ArticleDetailView', name='blog.article_detail'),
  #  url(r'^categorias/(?P<slug>[-\w]+)/$', 'blog.views.ProfileDetailView', name='blog.profile_detail'),
    url(r'^$', 'blog.views.inicio', name='blog.inicio'),
    url(r'^somos/$', 'blog.views.somos', name='blog.somos'),
    url(r'^blog/$', 'blog.views.blog', name='blog.blog'),
    url(r'^tour/$', 'blog.views.tour', name='blog.tour'),
    url(r'^tours/$', 'blog.views.tours', name='blog.tours'),
    url(r'^contacto/$', 'blog.views.contacto', name='blog.contacto'),
]