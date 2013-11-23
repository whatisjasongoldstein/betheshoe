from django.conf.urls import patterns, url

from .views import movie_detail

urlpatterns = patterns('',
    # url(r'^$', movie_list, name="index"),
    url(r'^(?P<slug>[-\w\d]+)/$', movie_detail, name="movies.detail"),
    # url(r'^(?P<slug>[-\w\d]+)/trailer/$', trailer, name="trailer"),
    # url(r'^(?P<slug>[-\w\d]+)/watch/$', watch_movie, name="watch"),
)