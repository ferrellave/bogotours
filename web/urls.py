from django.conf.urls import url
# -*- encoding: utf-8 -*-
from . import views

urlpatterns = [
    # /blog/ | /
 #   url(r'^$', views.ArticleListView.as_view(), name='web.article_list'),
 #   url(r'^@(?P<slug>[-\w]+)/$', 'web.views.UserProfileDetailView', name='web.userprofile_detail'),
  #  url(r'^publicacion/(?P<slug>[^\.]+)/$', 'web.views.ArticleDetailView', name='web.article_detail'),
  #  url(r'^categorias/(?P<slug>[-\w]+)/$', 'web.views.ProfileDetailView', name='web.profile_detail'),
    url(r'^$', 'web.views.home', name='web.home'),
    url(r'^somos/$', 'web.views.us', name='web.us'),
    url(r'^blog/$', 'web.views.blog', name='web.blog'),
    url(r'^blogs/$', 'web.views.blogs', name='web.blogs'),
    url(r'^tour/$', 'web.views.item', name='web.item'),
    url(r'^tours/$', 'web.views.items', name='web.items'),
    url(r'^contacto/$', 'web.views.contact', name='web.contact'),
]