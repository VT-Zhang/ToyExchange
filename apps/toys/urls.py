from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^goto$', views.goto, name='goto'),
    url(r'^goback$', views.goback, name='goback'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^add/(?P<id>\d+)$', views.add, name='add'),
    url(r'^image/(?P<id>\d+)$', views.image, name='image'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
