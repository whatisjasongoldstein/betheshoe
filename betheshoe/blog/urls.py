from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^$', 'betheshoe.blog.views.index', name="blog.index"),
    url(r'^(?P<slug>[\w-]+)/$', 'betheshoe.blog.views.post', name="blog.post"),
)