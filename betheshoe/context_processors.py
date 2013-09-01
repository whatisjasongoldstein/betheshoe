from django.contrib.sites.models import get_current_site

def current_site_url(request):
    return {
        "SITE_URL": get_current_site(request).domain,
    }