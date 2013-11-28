from django.conf.urls import patterns, url

from .views import movie_detail, movie_list

urlpatterns = patterns('',
    url(r'^$', movie_list, name="movies.index"),
    url(r'^(?P<slug>[-\w\d]+)/$', movie_detail, name="movies.detail"),
)