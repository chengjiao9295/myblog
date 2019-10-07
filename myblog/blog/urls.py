from django.conf.urls import url
from django.urls import path

from . import views
# https://www.jb51.net/article/136294.htm#_label5
app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]