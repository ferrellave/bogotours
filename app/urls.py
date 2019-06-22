from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = [
    url(r'^$', include('web.urls')),
    url(r'^', include('web.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns.append(
        url(
            regex=r'^uploads/(?P<path>.*)$',
            view='django.views.static.serve',
            kwargs={'document_root': settings.MEDIA_ROOT}))