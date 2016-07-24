from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^movies/(?P<slug>[-\w\d]+)/$', views.movie, name="movie"),
    url(r'^admin/', admin.site.urls),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
