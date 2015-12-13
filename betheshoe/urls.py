from django.conf import settings
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from .views import Index, Privacy
from .music.views import music_list
from .staff.views import staff_list

urlpatterns = [
    # Examples:
    url(r'^$', Index.as_view(), name='index'),
    url(r'^privacy/$', Privacy.as_view(), name='privacy'),
    url(r'^music/$', music_list, name='music'),
    url(r'^about/$', staff_list, name='about'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/crop/', include('cropper.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('betheshoe.blog.urls')),
    url(r'^movies/', include('betheshoe.movies.urls')),
    url(r'^draftin/webhooks/', include('draftin.urls')),

] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)