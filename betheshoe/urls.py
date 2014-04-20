from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.views.generic import TemplateView

from django.contrib import admin

from .views import Index, Privacy

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'betheshoe.views.home', name='home'),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^privacy/$', Privacy.as_view(), name='privacy'),
    url(r'^music/$', 'betheshoe.music.views.music_list', name='music'),
    url(r'^about/$', 'betheshoe.staff.views.staff_list', name='about'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/crop/', include('cropper.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('scruffy_blog.urls.blog')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^movies/', include('betheshoe.movies.urls')),

) + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)