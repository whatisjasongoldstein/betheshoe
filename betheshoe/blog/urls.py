from __future__ import absolute_import

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="blog.index"),
    url(r'^(?P<slug>[\w-]+)/$', views.post, name="blog.post"),
]